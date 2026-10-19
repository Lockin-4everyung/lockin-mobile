# Evidence Register

> Verified 19/10/2026 · [S] self-report survey; [D] published source; [I] inference; [P] planned research.

## S-01 - Survey provenance

Google Forms responses được dẫn trong ZIP; native Google Sheet, tab “Câu trả lời biểu mẫu 1”, sheetId 432431892. Đã đọc metadata, header A1:AJ1 và A2:AC113; có 12 responses thực ở rows 2–13, thu 08–12/10/2026 theo timestamps, timezone GMT+7. Không đọc giá trị cột AD (contact). Không download hoặc đưa raw dataset vào public repo.

12/12 là sinh viên và tự học gần đây theo screening. 8 năm 4, 4 năm 3. HCMUT-internal là bối cảnh theo ZIP; Sheet không đủ xác nhận từng người thuộc trường. Kênh phát, số lời mời, nonresponse và response rate chưa biết.

Public artifacts: [summary với cách đếm](../research/survey-summary.md), [aggregate JSON](../research/survey-summary.json). Không cần quyền đọc raw contact để kiểm tra các số đã công bố; raw giữ restricted cho người có quyền khi cần audit sâu.

## Finding IDs dùng xuyên suốt

| ID | Finding từ S-01 | Loại / denominator | Giới hạn và điều không được suy ra |
|---|---|---|---|
| E-01 | Q3 6 trễ + 2 bỏ giữa + 2 không học = 10/12; 1 thành công, 1 không nhớ. Q21/Q22: 52 dự định, 36 hoàn thành phần lớn; 9/12 dưới kế hoạch | Retrospective self-report, N=12 | Không đo prevalence toàn trường, frequency lâu dài hoặc completion quan sát |
| E-02 | Q6 8/12 từng hẹn; Q7 trong 8 người: 5 late, 1 no-show, 1 nhóm không học, 1 Other. Q8 4 “một chút” + 4 “rõ rệt” | Self-report; Q7/Q8 N=8 | Một incident/người, không phải thống kê 8 phiên ngẫu nhiên hoặc causal effect |
| E-03 | Q19 1/12 chọn app commitment; Q13 6/12 messaging đủ; Q10 6/12 chấm 4–5, mean 3,42 | Preference/intention, N=12 | Không phải 11 người chắc chắn từ chối app, không measured installs |
| E-04 | Q12 5 gần vô nghĩa + 2 yếu nhiều = 7/12 khi khác phòng | Hypothetical evaluation | Không rõ tất cả hiểu phòng vật lý hay online; shared view còn hypothesis |
| E-05 | Q15 public room: 4/12 chấm 4–5, 6/12 chấm 1–2, 2/12 chấm 3 | Intention, N=12 | Không đại diện phân khúc thích strangers |
| E-06 | Q13 3/12 lo áp lực; 2/12 không muốn lộ vắng/bỏ sớm | Multi-select preference | Không phải consent chia sẻ trạng thái thật |
| E-07 | Q20 5/12 cài nếu hữu ích; 4/12 nếu bạn dùng; 1/12 muốn thử web; Q13 4/12 ngại nhiều thao tác | Conditional intention | Không chứng minh low-friction adoption/repeat |
| E-08 | Q18 8/12 chọn invite, 6/12 own reminder, 1/12 gợi ý public room, 1/12 không muốn notification | Multi-select preference | Không chứng minh reminder làm tăng attendance |

**Không gộp:** N=8 ở branching với N=12; multi-select với single-select; preference với hành vi; tổng số phiên với số người; check-in với học hiệu quả. Một Q5 option chứa dấu phẩy nên không tách chuỗi bằng mọi dấu phẩy để đếm; dùng nhãn option đầy đủ/substrings phân biệt.

## Desk research thực hiện lại ngày 19/10/2026

| ID | Nguồn chính thức | Claim được hỗ trợ | Giới hạn |
|---|---|---|---|
| D-01 | [Discord Scheduled Events](https://support.discord.com/hc/en-us/articles/4409494125719-Scheduled-Events) | Event, Interested/RSVP, link và thông báo khi event live | Không chứng minh task tự học nhanh/chậm; Interested không giống ba trạng thái Yes/No/Maybe |
| D-02 | [Google Calendar - Invite people](https://support.google.com/calendar/answer/37161?hl=en) | Email invite, Yes/No/Maybe, response tracking và reminder theo cài đặt khách | Không phải hands-on benchmark |
| D-03 | [Focusmate - How it works](https://www.focusmate.com/how-it-works/) | Booking partner, video-on, goals/check-in, 25/50/75 phút | Không chứng minh target LockIn thích camera hay strangers |
| D-04 | [StudyStream Focus rooms](https://help.studystream.live/hc/help/articles/1788197098-focus-rooms-everything-you-can-do); [Spaces](https://help.studystream.live/hc/help/articles/1786624910-spaces-study-together-and-talk-in-a-focus-room) | Silent rooms, chat, Spaces; Spaces chỉ desktop web, Pods mobile tạm unavailable | Availability có thể đổi; không suy room là USP |
| D-05 | [YPT Google Play listing](https://play.google.com/store/apps/details?id=com.pallo.passiontimerscoped) | Timer/todo, groups/status, rankings/stats, app blocking Android | Nội dung do developer công bố, chưa kiểm thử permissions/tính ổn định |
| D-06 | [Forest official site](https://www.forestapp.cc/) | Focus timer, blocking và Plant Together | Không suy LockIn tốt hơn, availability tùy platform/version |
| D-07 | [React Native AppState](https://reactnative.dev/docs/appstate) | Foreground/background state API | Không phát hiện người có học hay đang dùng app cụ thể; framework chưa chốt |

Phân tích và implications tại [2.6](06-Existing-Solutions-Alternatives.md), không chỉ feature table. Không dùng lời quảng cáo, download count hay lời hứa tăng năng suất làm bằng chứng hiệu quả.

## Evidence chưa tồn tại

Interview notes, task times, pilot attendance, measured repeats và willingness to pay chưa có. [Protocol](18-Research-Protocol.md) chỉ là template; không dùng ID S-02 hoặc số kết quả tưởng tượng. Mọi claim mới cần provenance/date/method/limitations trước khi thêm decision.
