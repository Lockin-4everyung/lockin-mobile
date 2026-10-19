# 2.7. Evidence Evaluation & Product Decisions

> 19/10/2026 · Quyết định đề xuất; chưa có team sign-off hoặc kết quả thử sản phẩm.

| Assumption | Evidence | Giới hạn | Decision | Hệ quả |
|---|---|---|---|---|
| A1: pain đủ thường xuyên/đáng đổi workflow | E-01: 10/12 trục trặc lần gần nhất; 9/12 dưới kế hoạch tuần | Self-report; chưa đo tần suất/độ nghiêm trọng dài hơn; 1 người không nhớ | **Investigate further** | Giữ problem để nghiên cứu, không nói đã validate tần suất |
| A2: người quen tăng trách nhiệm | E-02: 8/8 người từng hẹn cảm nhận trách nhiệm tăng | Self-selection, không đối chứng | **Investigate further** | Đo hành vi trong pilot, chưa nói tăng completion |
| A3/H1: giá trị vượt alternatives | E-03: 1/12 ưu tiên app; 6/12 thấy messaging đủ; D-01/D-02 | Forced-choice không đo adoption thực; desk research không đo UX | **Investigate further** | Task comparison và repeat là ưu tiên |
| A4: không cần cùng phòng | E-04: 7/12 thấy suy yếu nhiều/gần vô nghĩa | Giả định tình huống; cách hiểu phòng chưa rõ | **Revise** | Thử shared session nhẹ; hỏi lại cách hiểu |
| A5: public room là entry point | E-05: 4/12 chấm 4–5, 6/12 chấm 1–2; D-04 | Mẫu chưa đại diện người thích strangers | **Revise** | Bỏ public room khỏi MVP; defer là hành động, không phải nhãn decision thứ năm |
| A6: đồng ý chia sẻ trạng thái | E-06: 3/12 lo áp lực; 2/12 không muốn lộ vắng/bỏ sớm | Preference, chưa phải consent thực | **Investigate further** | Quyền theo commitment; thử hiểu biết về visibility |
| A7: join ít friction | E-07: 5/12 cài nếu hữu ích, 4/12 nếu bạn dùng; Q13 có 4/12 ngại thao tác | Ý định không phải installs/repeat | **Investigate further** | Join tối giản; không xây friend graph phức tạp |
| A8: reminder ít phiền | E-08: 8/12 chọn invite, 6/12 nhắc phiên mình, 1/12 gợi ý room; 1/12 không muốn thông báo | Multi-select, chưa quan sát phản ứng | **Revise** | Reminder trực tiếp, opt-out và lịch trong app |

[Evidence Register](16-Evidence-Register.md) định nghĩa E-01–E-08. Bảng này sửa lỗi ZIP: A6 là privacy nhưng từng bị đánh giá bằng notification preference; notifications nay là A8.

## Direction tiếp theo

MVP thử lời hẹn với bạn quen: giờ rõ → mời → nhận lời → nhắc → check-in → outcome tự báo cáo. Friend-first, camera-optional và shared view là giả thuyết định vị. Hoãn public discovery, matching, feed, chat/video riêng, leaderboard và blocking.

Mobile hợp tương tác ngắn/nhắc giờ nhưng chưa chứng minh đáng cài app mới. Nếu H1 bị challenge theo [protocol](04-Evidence-Plan.md), Revise sang link/web hoặc bổ trợ công cụ quen; nếu pain nhỏ và alternatives đủ, cân nhắc Reject app độc lập. Hiện chưa đủ evidence để Reject hoàn toàn một assumption.

## Decision log

| Ngày | ID | Thay đổi | Căn cứ | Xác nhận |
|---|---|---|---|---|
| 19/10/2026 | DEC-01 | A3 vẫn riskiest; chưa tuyên bố validation | E-03, D-01/D-02 | Đề xuất, chờ team review |
| 19/10/2026 | DEC-02 | Hoãn public room, thử shared view | E-04/E-05, D-04 | Đề xuất, chờ team review |
| 19/10/2026 | DEC-03 | Not confirmed thay kết luận no-show tự động | Bản ghi check-in có thể thiếu do mất mạng/không mở app | Đã sửa tài liệu, chờ review sản phẩm |
| 19/10/2026 | DEC-04 | A6 giữ privacy, thêm A8 | Mâu thuẫn ID trong ZIP | Đã sửa tài liệu |
| 19/10/2026 | DEC-05 | Thêm 2.12, tasks và submission gate | Requirement 2.12, sections 4/6 | Đã chuẩn bị local; GitHub chưa cập nhật |
