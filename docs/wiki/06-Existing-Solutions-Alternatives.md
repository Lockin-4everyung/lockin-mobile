> **LockIn · CO3043 · Assignment 1 · Revised 19/10/2026**  
> Survey: 12 respondents (HCMUT internal); [S] survey, [D] desk research, [I] inference, [P] future test.

## 2.6. Existing Solutions & Alternatives

**Phương pháp:** desk research trên website/help center/store listing chính thức, đối chiếu lại **19/10/2026**; kết hợp dữ liệu Q5/Q19/Q13 từ survey. Đây là **đối chiếu mô tả tính năng được công bố**, chưa phải usability benchmark do nhóm trực tiếp thử các sản phẩm. Các cột “gap” là **nhận định cần kiểm chứng**, không được xem là bằng chứng rằng đối thủ hoàn toàn không có chức năng tương tự.

### Tổng quan đối thủ / giải pháp thay thế

| Giải pháp | Nhóm | Điều đã đáp ứng tốt (có nguồn) | Giới hạn đối với use case LockIn / điều cần kiểm tra | Insight cho LockIn |
|---|---|---|---|---|
| **Discord (chat + Scheduled Events)** | Thay thế trực tiếp/gián tiếp | Chat/voice channels; Scheduled Events có thông báo và cơ chế bày tỏ quan tâm, đường dẫn sự kiện và RSVP | Có thể đã xử lý nhiều khâu scheduling/RSVP; trải nghiệm check-in/completion dành riêng cho tự học cần được **so sánh bằng task test** | Không được quảng bá “Discord không có RSVP”; LockIn phải giảm friction hoặc cải thiện follow-through đáng kể |
| **Google Calendar** | Thay thế gián tiếp mạnh | Mời người qua email; Yes/No/Maybe, xem RSVP, reminders | Việc ghi nhận check-in/học xong theo phiên tự học không phải task được nhấn mạnh trong tài liệu Calendar; không suy ra thiếu hoàn toàn cách tích hợp | Nếu chỉ có thời gian + RSVP thì LockIn chưa tạo khác biệt đủ rõ |
| **Focusmate** | Direct accountability alternative | Đặt phiên 25/50/75 phút, ghép partner, video cùng làm việc, chia sẻ goal và check-in cuối buổi | Camera/video là điểm khác biệt về trải nghiệm và quyền riêng tư; LockIn muốn *camera-optional, friend-first* cần chứng minh có lợi trong target | Accountability có thể được sản phẩm hóa, nhưng phải so sánh điều kiện video và làm việc với người lạ |
| **StudyStream** | Direct social-focus alternative | Focus rooms, room silent, chat; có Spaces cho nhóm nhỏ trên desktop web | Public room và nhóm đã tồn tại; Spaces chỉ desktop web, Pods mobile tạm ngừng theo help center | Hoãn đầu tư public room; nếu làm nhóm quen phải giữ trải nghiệm đơn giản và mobile-friendly |
| **YPT / Yeolpumta** | Direct study-tracking alternative | Study timer, to-do, nhóm bạn, trạng thái nhóm, rankings, stats; Android listing có chức năng block apps gây xao nhãng | LockIn không nên đua tracking/leaderboard/blocker về feature count; cần test “commitment với RSVP theo buổi” có lợi gì mới | Khác biệt dự kiến nằm ở **cam kết theo thời điểm và theo người**, không phải timer/blocking |
| **Forest** | Solo focus / nhóm thay thế | Focus timer, cây/động lực trực quan, Deep Focus/app blocking, và tính năng plant together | Đã mạnh về chống xao nhãng và có yếu tố bạn bè; chưa đủ cơ sở để nói LockIn tốt hơn nếu chỉ đếm thời gian học | OS-level app blocking nên là feature nghiên cứu riêng, không nằm MVP commitment |
| **Thư viện/quán cà phê** | Giải pháp offline | Không gian học và hiện diện xã hội trực tiếp; Q19 có 3/12 chọn đây là phương án ưu tiên | Phụ thuộc địa điểm/chi phí/thời gian di chuyển; với nhiều sinh viên vẫn là lựa chọn đủ tốt | LockIn không nên cố thay thế mọi tình huống; phù hợp hơn với học ở nhà/khó di chuyển nhưng vẫn trùng giờ |

### 1) Discord - đâu là vấn đề còn mở?

- **Dữ kiện `[D]`:** Discord hỗ trợ voice channels và Scheduled Events; các event có thể gửi nhắc cho người quan tâm, có đường dẫn tham gia và khả năng RSVP trong ngữ cảnh server. [Nguồn: Discord Scheduled Events](https://support.discord.com/hc/en-us/articles/4409494125719-Scheduled-Events).
- **Dữ kiện `[S]`:** 6/12 chọn “Messenger/Zalo/Discord đã đủ” là một lo ngại; 3/12 ưu tiên hẹn bạn qua nhắn tin trong lựa chọn Q19.
- **Điều chưa biết `[I]`:** việc tạo server event có nặng với một lời hẹn học 2–3 người không? Check-in/early-leave tracking có đáng giá hơn chat thông thường không?
- **Hệ quả:** lấy Discord và chat-group thông thường làm **baseline task** khi test; không so sánh bằng feature list chung chung.

### 2) Google Calendar - một alternative thường bị bỏ qua

- **Dữ kiện `[D]`:** Calendar mời khách qua email, hiển thị trạng thái Yes/No/Maybe, hỗ trợ event reminders và theo dõi phản hồi. [Nguồn: Google Calendar Help - Invite guests](https://support.google.com/calendar/answer/37161?hl=en); [Response tracking trong cùng hướng dẫn](https://support.google.com/calendar/answer/37161?hl=en).
- **Điều chưa biết `[I]`:** người học có chịu tạo calendar event cho mỗi phiên không; trạng thái RSVP có đủ hay vẫn cần check-in theo phiên?
- **Hệ quả:** nếu LockIn chỉ tái hiện lịch + reminder + RSVP, lợi thế cạnh tranh chưa rõ. Workflow phải *đúng ngữ cảnh tự học và giảm thao tác*.

### 3) Focusmate - accountability mạnh nhưng khác điều kiện tham gia

- **Dữ kiện `[D]`:** đặt phiên, ghép partner, sử dụng video và trao đổi mục tiêu/tiến độ đầu-cuối; thời lượng 25/50/75 phút; không suy diễn check-in thành chứng minh chất lượng công việc. [Nguồn: How it works](https://www.focusmate.com/how-it-works/).
- **Điều chưa biết `[I]`:** sinh viên LockIn có muốn camera-on khi học, thích người quen hay người lạ hơn; họ có sẵn lòng book phiên như Focusmate không?
- **Hệ quả:** mô hình “known friends + không bắt buộc video” là *giả thuyết định vị*, không được khẳng định đã vượt Focusmate.

### 4) StudyStream - public room không phải điểm khác biệt mới

- **Dữ kiện `[D]`:** focus room nhiều người, silent by design; có room chat, số người tham gia, các hình thức hiển thị; Spaces cho nhóm nhỏ trên web với voice/chat/task list. Tài liệu hiện ghi Spaces/Pods chưa hoạt động trong mobile app. [Nguồn: Focus rooms](https://help.studystream.live/hc/help/articles/1788197098-focus-rooms-everything-you-can-do); [Spaces](https://help.studystream.live/hc/help/articles/1786624910-spaces-study-together-and-talk-in-a-focus-room).
- **Dữ kiện `[S]`:** Q15 chỉ 4/12 đánh giá public room 4–5/5; 6/12 chấm 1–2/5.
- **Hệ quả:** public room chỉ nên có trong roadmap thử nghiệm khi đã thấy nhu cầu, không coi là MVP dependency.

### 5) YPT - đối thủ trực tiếp cho time tracking và group status

- **Dữ kiện `[D]`:** app có study timer, subject tracking, study groups, rank/stats và (trên Google Play Android listing) app-blocking. [Nguồn: Google Play YPT](https://play.google.com/store/apps/details?id=com.pallo.passiontimerscoped).
- **Hệ quả:** LockIn không cần chế lại một YPT nhỏ; chỉ thêm tracking, streak, leaderboard nếu sau này có evidence cho các hoạt động đó.

### 6) Forest - app blocking không còn là khoảng trống hiển nhiên

- **Dữ kiện `[D]`:** Forest cung cấp focus sessions và Deep Focus/app-blocking; có cơ chế “plant together” ở nhóm. [Nguồn: Forest](https://www.forestapp.cc/).
- **Hệ quả:** app blocking đòi native permissions, policy và test hệ điều hành; giá trị chính của Assignment 1 vẫn là kiểm chứng commitment, không phải sao chép cơ chế blocker.

### Tổng hợp khoảng trống có thể kiểm chứng

1. **Không thiếu** công cụ lên lịch, RSVP, Pomodoro, online room hay app blocking. `[D]`
2. Khoảng trống *có thể tồn tại*, nhưng chưa được chứng minh, là **một luồng cực ngắn dành riêng cho nhóm bạn quen tự hẹn học, hiển thị RSVP và check-in/completion dễ hiểu, không bắt camera/call**. `[I]`
3. Lợi thế này sẽ chỉ có giá trị nếu **không tăng gánh nặng cài app, tạo nhóm, mời nhau**. `[S]` `[I]`
4. **Cần thử trực tiếp**: một kịch bản hẹn học 20:00–21:00 được thực hiện bằng Discord/Calendar và bằng prototype LockIn; đếm bước, thời gian, lỗi hiểu nhầm, mức muốn dùng lại. `[P]`

---

Xem [Evidence Register](16-Evidence-Register.md), [Traceability](14-Traceability-Matrix.md) và [Project Plan](13-Project-Foundation-Plan.md).
