> **LockIn · CO3043 · Assignment 1 · Revised 19/10/2026**  
> Survey: 12 respondents (HCMUT internal); [S] survey, [D] desk research, [I] inference, [P] future test.

## 2.2. Mobile Product Rationale

### Vì sao mobile là một nền tảng hợp lý `[I]`

| Nhu cầu thực tế | Điều mobile có thể hỗ trợ | Lợi ích kỳ vọng | Giới hạn |
|---|---|---|---|
| Nhận và phản hồi lời mời khi không ngồi máy tính | Thiết bị cá nhân, deep link, quick interaction | Giảm thời gian xác nhận | Người được mời có thể chưa cài app |
| Nhớ cam kết sắp đến giờ | Local/remote notifications, lịch | Nhắc đúng bối cảnh trước giờ học | Push có thể trễ, bị tắt hoặc không giao |
| Check-in khi phiên bắt đầu | Một màn hình check-in ngắn | Giảm thao tác | Check-in không chứng minh thực sự học |
| Theo dõi sự tham gia với bạn | Dữ liệu đồng bộ, cập nhật trạng thái | Biết ai đã nhận lời/đến giờ | Cần tôn trọng quyền riêng tư, tránh áp lực xã hội |
| Rời/quay lại ứng dụng | [React Native AppState](https://reactnative.dev/docs/appstate) (nếu chọn framework này) | Nhận biết app ở foreground/background | **Không xác định được người dùng đang học hay mở app nào**, nên không dùng để kết luận mất tập trung |

### Các lựa chọn không dùng app riêng

- **Messenger/Zalo/Discord:** lợi thế mạng lưới người dùng sẵn có, trao đổi linh hoạt; Discord còn có Scheduled Events và RSVP trong server. Xây thêm app có thể tăng friction thay vì giảm. `[S]` `[D]`
- **Google Calendar:** tạo sự kiện, mời người qua email, theo dõi Yes/No/Maybe và nhắc lịch; đã đáp ứng một phần rất lớn chức năng lên lịch/RSVP. `[D]`
- **Web/PWA hoặc invite link:** ít yêu cầu cài đặt, thuận tiện thử nghiệm ban đầu. Hiện chưa có dữ liệu chứng minh native mobile thắng cách này. `[I]`

**Kết luận:** mobile phù hợp với tương tác ngắn, cá nhân và nhắc đúng lúc, **nhưng chưa chứng minh đủ giá trị của việc cài một app mới**. MVP nên đo được *time-to-invite, time-to-RSVP, effort, attendance và willingness-to-repeat* khi so với chat/lịch. Không dùng lập luận “vì đây là môn Mobile Application Development”.

---

Xem [Evidence Register](16-Evidence-Register.md), [Traceability](14-Traceability-Matrix.md) và [Project Plan](13-Project-Foundation-Plan.md).
