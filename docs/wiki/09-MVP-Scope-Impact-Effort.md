# 2.9. MVP Scope & Impact–Effort Matrix

> 19/10/2026 · Scope để thiết kế và kiểm chứng H1, chưa phải sản phẩm đã triển khai.

## Primary goal và core value path

“Tôi muốn hẹn tự học với 1–3 bạn quen, biết ai nhận lời và có bản ghi tham gia rõ ràng mà không phải điều phối nhiều tin nhắn.”

**Xem lịch → đặt giờ → mời → Accept/Decline → nhắc/xem phiên → check-in → shared participant view → tự báo kết quả.** Creator cũng là participant và phải tự check-in; tạo phiên không tự xác nhận có mặt.

## Cách chấm Impact–Effort [I]

Impact: 3 = thiếu thì core path/H1 không kiểm tra được; 2 = giúp nhớ/đánh giá follow-through; 1 = phụ hoặc chưa rõ nhu cầu. Effort là ước lượng person-day sơ bộ: S 0,5–1; M 2–3; L 4–5; XL >5. Không phải benchmark hay cam kết năng lực nhóm. Quyền dữ liệu/sync tính trong estimate tính năng, không cộng hai lần.

| | Effort S/M | Effort L/XL |
|---|---|---|
| Impact 3 | F-01 lịch/giờ; F-03 RSVP; F-04 check-in; F-05 shared view; F-08 hủy trước phiên | F-02 identity và invite có quyền |
| Impact 2 | F-06 reminder; F-07 outcome; usability instrumentation tối thiểu | Remote push tự động và deferred deep link đầy đủ |
| Impact 1 / chưa rõ | Streak cá nhân; timer trang trí | Public directory/matching; chat/video; leaderboard; blocking |

F-02 effort cao vẫn cần cho coherent path: không mời/nhận lời an toàn thì không thử được H1. F-07 chỉ impact 2 nhưng là tín hiệu học tập của pilot, chi phí nhỏ. F-06 giữ vì mobile rationale; remote push tự động chưa bắt buộc khi lời mời có thể chia sẻ qua công cụ quen.

## Minimum coherent scope

| ID | Feature / need | Trace | Impact / effort | Quyết định |
|---|---|---|---|---|
| F-01 | Lịch của mình và tạo commitment: giờ tương lai, start/end/timezone rõ | E-01/E-02/E-03 → R-01 → US-01/US-09 | 3 / M (3 ngày) | MVP |
| F-02 | Identity tối giản và mời 1–3 bạn đã xác định, link không làm lộ roster | E-03/E-06/E-07 → R-02/R-07 → US-02/US-03/US-08 | 3 / L (5) | MVP enabler, không xây social graph |
| F-03 | Pending/Accepted/Declined/Expired; không auto-Accept | E-02/E-03 → R-02 → US-02/US-03 | 3 / M (2) | MVP |
| F-04 | Check-in có xác nhận server, Late/Not confirmed rõ | E-02/H1 → R-04 → US-05 | 3 / M (3) | MVP |
| F-05 | Một session của nhóm, giờ còn lại và bản ghi check-in; không khẳng định live presence | E-04 → R-05 → US-06 | 3 / M (2) | MVP giả thuyết cần test |
| F-06 | Reminder tùy chọn trước giờ, lịch trong app khi không có quyền | E-08 → R-03 → US-04/US-09 | 2 / M (3) | MVP; local reminder trước |
| F-07 | Completed/Left early/Unconfirmed tự báo; lịch sử ngắn của mình | H1 [P] → R-06 → US-07 | 2 / M (2) | MVP để đo follow-through |
| F-08 | Creator hủy trước start; vô hiệu lời mời/nhắc cũ | Rủi ro lời hẹn thay đổi [I] → R-08 → US-10 | 3 / M (2) | MVP; đổi giờ bằng hủy rồi tạo mới |

Khoảng **22 person-day** development sơ bộ cho F-01–F-08, chưa gồm 4 ngày thiết kế, 5 ngày kiểm thử, 4 ngày phân tích/review và các ngày lịch chạy nghiên cứu. [Project plan](13-Project-Foundation-Plan.md) đã có roster 4 người, nhưng capacity và người phụ trách implementation chưa chốt nên chưa chứng minh đủ nguồn lực. [Project Architecture](19-Project-Architecture.md) chọn React Native + Expo + TypeScript và Supabase làm hướng triển khai; T-07 vẫn phải xác minh thiết bị, identity/invite và effort trước khi khóa kế hoạch build.

## Quy tắc sản phẩm dùng chung

- [State rules và check-in window](17-Product-Rules-Metrics.md) là bản đề xuất thống nhất cho stories/flows/protocol.
- Chỉ creator và Accepted participants xem roster/outcome của nhóm. Pending invitee có quyền xem tối thiểu inviter, giờ và mục đích để quyết định; người ngoài không thấy dữ liệu. Declined/Expired mất quyền phiên.
- Link không tự cấp toàn quyền; xác thực đúng invitee trước RSVP. Kiến trúc chọn email OTP và đối chiếu email của lời mời; T-07 phải kiểm chứng friction và access trên thiết bị thật.
- Check-in cần server acknowledgement. Offline giữ trạng thái chưa gửi và retry khi còn trong window; không chấp nhận client clock như bằng chứng đúng giờ.
- Background/đóng app/đọc PDF không đồng nghĩa rời phiên hoặc vắng học. Không dùng AppState để đánh giá tập trung.
- Người dùng chủ động Left early hoặc Completed; không thao tác thì Unconfirmed. Không công khai bảng phạt/no-show.

## Exclusions và điều kiện giảm scope

Public rooms/matching, social feed, in-app chat/call/camera, OS blocking, leaderboard/streak, monetization, friend discovery và tự động nhận biết đang học đều ngoài MVP. Remote push cho lời mời, edit-time phức tạp và đồng bộ offline backdate cũng hoãn.

Nếu invite/onboarding quá nặng, giảm xuống prototype/link thử H1 trước. Nếu reminder bị từ chối, vẫn có lịch. Nếu sync không tin cậy, dừng suy luận attendance và sửa trước pilot. Nếu không đủ capacity, giảm participant count/platform hỗ trợ trước; giữ trọn create → invite → RSVP → check-in → outcome để còn kiểm tra core value.
