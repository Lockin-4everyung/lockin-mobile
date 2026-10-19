# 2.11. Critical User Flows

> 19/10/2026 · Logic sản phẩm, chưa thiết kế UI chi tiết. Window và quyền ở [Product Rules](17-Product-Rules-Metrics.md).

## FL-01 - Tạo, mời và trả lời

Stories: US-01/02/03/08/09/10. Tasks: T-07/08/09/10/14.

~~~mermaid
flowchart TD
    A(["Bắt đầu: muốn hẹn học với bạn"]) --> B["Mở lịch và chọn start/end"]
    B --> C{"Giờ tương lai và end sau start?"}
    C -- "Không" --> B
    C -- "Có" --> D["Chọn 1–3 invitee xác định"]
    D --> E["Lưu phiên: creator Accepted, invitee Pending"]
    E --> F{"Server đã xác nhận lưu?"}
    F -- "Không" --> G["Giữ dữ liệu và thử lại cùng request"]
    G --> E
    F -- "Có" --> H["Chia sẻ link mời qua công cụ quen"]
    H --> I{"Invitee mở link?"}
    I -- "Chưa" --> J["Giữ Pending đến start"]
    J --> K(["Đến start: Expired, không tự Accept"])
    I -- "Có" --> L["Xác thực đúng invitee, giữ lời mời qua onboarding"]
    L --> M{"Đúng quyền, phiên chưa hủy và còn trước start?"}
    M -- "Không" --> N(["Kết thúc: invalid, expired hoặc wrong-user"])
    M -- "Có" --> O["Xem inviter, giờ và giải thích visibility"]
    O --> P{"Chọn Accept hay Decline?"}
    P -- "Decline" --> Q["Lưu Declined, đóng quyền xem phiên"]
    P -- "Accept" --> R["Lưu Accepted, mở roster và thêm lịch"]
    R --> S{"Server xác nhận RSVP?"}
    Q --> S
    S -- "Chưa" --> T["Hiện chưa gửi, cho retry trước start"]
    T --> M
    S -- "Rồi" --> U(["Kết thúc: trạng thái rõ, không coi là có mặt"])
    E -. "Creator hủy trước start" .-> V["Cancelled, thu hồi lời mời và nhắc"]
    V --> W(["Kết thúc: thông báo kế hoạch đã hủy"])
~~~

Không ai nhận lời thì creator có thể mời tiếp trước start hoặc hủy. Sau start không nhận thêm RSVP trong MVP. Gửi trùng/lưu trùng dùng cùng request, không tạo commitment mới khi retry. Conflict lịch chỉ cảnh báo; không truy cập lịch cá nhân bên ngoài.

## FL-02 - Nhắc, check-in và tự báo kết quả

Stories: US-04/05/06/07/08/09. Tasks: T-11/12/13/14/15.

~~~mermaid
flowchart TD
    A(["Bắt đầu: Accepted, phiên không hủy"]) --> B["Xem lịch; reminder nếu đã cho phép"]
    B --> C{"Đến start trừ 5 phút?"}
    C -- "Chưa" --> D["Xem giờ và chờ"]
    D --> C
    C -- "Rồi" --> E{"Chọn check-in trước end?"}
    E -- "Không" --> F["Đến end: Not confirmed, không kết luận no-show"]
    E -- "Có" --> G["Gửi check-in"]
    G --> H{"Server nhận và còn trong window?"}
    H -- "Chưa, còn thời gian" --> I["Chưa gửi hoặc offline; retry"]
    I --> G
    H -- "Hết window" --> F
    H -- "Có" --> J{"Nhận trước hoặc bằng start cộng 5 phút?"}
    J -- "Có" --> K["On-time confirmed"]
    J -- "Không" --> L["Late confirmed"]
    K --> M["Xem timer và bản ghi thành viên"]
    L --> M
    M --> N{"Chủ động rời sớm trước end?"}
    N -- "Có" --> O["Xác nhận Left early, tự báo cáo"]
    N -- "Không" --> P{"Đến end?"}
    P -- "Chưa" --> M
    P -- "Rồi" --> Q{"Báo Completed?"}
    Q -- "Có" --> R["Lưu Completed, tự báo cáo"]
    Q -- "Không" --> S["Unconfirmed outcome"]
    O --> T(["Kết thúc: lịch sử ghi điều đã báo"])
    R --> T
    S --> T
    F --> T
~~~

Outcome vẫn cần server acknowledgement; nếu không gửi được, hiển thị pending và retry, chưa hiện là đã lưu. Thiếu bản ghi do offline không chứng minh người học vắng. Background, khóa máy, đọc PDF hoặc code không đổi participant outcome. Creator cũng đi qua cùng flow check-in.

## Review logic đã đối chiếu trong tài liệu

- FL-01 có lỗi giờ, save/retry, người chưa onboard, quyền sai, invitation hết hạn, không trả lời, decline và hủy.
- FL-02 có on-time, late, không xác nhận, offline/retry, rời sớm và outcome thiếu.
- Không có transition từ AppState sang đánh giá học tập.
- Privacy và source of truth thống nhất với stories; usability trên người thật còn là T-04, chưa chạy.
