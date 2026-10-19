# Survey summary - public aggregate

Đối chiếu Google Sheet ngày **19/10/2026**, 12 phản hồi thu **08–12/10/2026**. Đọc tab “Câu trả lời biểu mẫu 1”, header A1:AJ1 và responses A2:AC113; có dữ liệu ở rows 2–13. Không đọc giá trị cột AD có contact, không lưu raw rows. [Machine-readable aggregate](survey-summary.json).

Kết quả là tự báo cáo của mẫu hẹp; HCMUT-internal theo ZIP, chưa xác minh affiliation từng người. Kênh tuyển và response rate chưa có record.

| Câu / phép đếm | Kết quả | Denominator / diễn giải |
|---|---|---|
| Screening sinh viên/tự học gần đây | 12 Có cho mỗi câu | N=12 |
| Q1 | 8 năm 4, 4 năm 3 | Không có năm 1–2 |
| Q3 lần gần nhất | 6 trễ, 2 bỏ giữa, 2 không học, 1 thành công, 1 không nhớ | 10/12 có trục trặc; không phải frequency toàn trường |
| Q4 lý do, multi-select | Mệt 8, phone/entertainment 7, khó bắt đầu 6 | Không chứng minh commitment giải quyết được các nguyên nhân |
| Q5 hỗ trợ, multi-select | Solo 7; todo 5; library/cafe 4; friends 3; calls 2; blocker 2; Pomodoro 1; Discord/room 1 | Một option chứa dấu phẩy; đếm theo nhãn thay vì split mọi dấu phẩy |
| Q6 | 8 từng hẹn bạn, 4 chưa | N=12 |
| Q7 | 5 late, 1 no-show, 1 cả nhóm không học, 1 Other | N=8 theo branching, không chia 12 |
| Q8 | 4 tăng trách nhiệm một chút, 4 rõ rệt | N=8, cảm nhận không phải causal effect |
| Q7B | 4/4 thích solo; 1/4 còn thấy hẹn phiền | N=4 chưa từng hẹn |
| Q10 hữu ích 1–5 | 1:1, 2:0, 3:5, 4:5, 5:1; mean 41/12 = 3,42 | 6/12 chấm 4–5 |
| Q11 giá trị chính | Giờ rõ 4; check-in 3; accepted 2; no-show/left-early 1; history 1; không phần nào 1 | Single-select, tổng 12 |
| Q12 khác phòng | Gần vô nghĩa 5; yếu nhiều 2; yếu chút 3; gần không khác 2 | 7/12 phản đối mạnh; cách hiểu “phòng” cần hỏi lại |
| Q13 concerns | Messaging đủ 6; nhiều thao tác 4; khó trùng giờ 5; áp lực 3; visibility 2 | Multi-select, không phải consent |
| Q15 public room | 1:4, 2:2, 3:2, 4:3, 5:1 | 4/12 high; 6/12 low |
| Q18 notifications | Invite 8; own reminder 6; public suggestion 1; không muốn notification 1 | Multi-select |
| Q19 ưu tiên | Messaging 3; library/cafe 3; calls 2; timer 2; app commitment 1; không cần thêm 1 | Single-select |
| Q20 cài app | 5 nếu hữu ích; 4 nếu bạn dùng; 1 tùy lúc; 1 thử web trước; 1 không muốn cài | Intention, không measured installs |
| Q21/Q22 | 52 dự định; 36 hoàn thành phần lớn; 9 người dưới kế hoạch | 36/52 = 69,23% tổng phiên hồi tưởng, không mean completion của từng người |
| Hai feedback mở | 6 người có nội dung ở ít nhất một cột; 1 chỉ “không có”, 5 có góp ý nội dung | Deduplicate theo người, không dùng số ô thành số người |
| Q23 follow-up | 2 Có, 9 Không, 1 trống | Không đọc hoặc công khai contact |

## Calculation notes

- Planned total = SUM(Q21); completed total = SUM(Q22); below-plan = COUNT(Q22 < Q21). Đây là tổng hồi tưởng, không log app.
- Rating high = COUNT(value >= 4); public low = COUNT(value <= 2). Mean Q10 = 41/12.
- Q7/Q8 chỉ người có lịch hẹn; 4 blank do branching không phải 4 “không”.
- Multi-select đếm mỗi người tối đa một lần mỗi option; tổng option có thể vượt 12.
- Feedback nội dung chỉ tổng hợp themes: alternatives đủ, thiếu ràng buộc, thiếu cảm giác cùng học, nguy cơ quấy rối public room và muốn tương tác. Không công bố verbatim quotes hoặc tần suất theme chưa code độc lập.

Xem [phân tích, contradictions và limitations](../wiki/05-User-Market-Research.md) và [Evidence Register](../wiki/16-Evidence-Register.md). Các nghiên cứu mới ở protocol chưa chạy.
