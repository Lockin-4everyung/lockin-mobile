# Traceability Matrix

> 19/10/2026 · Mỗi hàng nối tới development work thực. [Evidence](16-Evidence-Register.md), [stories](10-User-Stories.md), [features](09-MVP-Scope-Impact-Effort.md), [flows](11-Critical-User-Flows.md), [tasks](13-Project-Foundation-Plan.md).

Evidence có thể dẫn tới hypothesis/requirement thử nghiệm, không tự biến thành nhu cầu đã được xác nhận.

| Evidence / hypothesis | User need | Requirement | Story | MVP feature | Flow | Development / validation task |
|---|---|---|---|---|---|---|
| E-01/E-02; Q11 4/12 coi giờ rõ quan trọng | N-01: hẹn không mơ hồ | R-01: lịch cá nhân, start/end hợp lệ, timezone rõ | US-01, US-09 | F-01 | FL-01, FL-02 | T-09,T-14 |
| E-02: late/no-show tự báo; E-03/E-07: alternatives và friction | N-02: biết ai nhận lời, không phải nhắn lặp | R-02: identity/invite/RSVP rõ, ít thao tác | US-02, US-03 | F-02,F-03 | FL-01 | T-07,T-10,T-04 |
| E-08: 6/12 chọn own reminders; 1/12 không muốn thông báo | N-03: nhớ đúng giờ, tránh phiền | R-03: reminder tùy chọn và lịch fallback | US-04, US-09 | F-06,F-01 | FL-02 | T-11,T-14 |
| E-02; Q11 3/12 chọn check-in; H1 chưa kiểm chứng | N-04: có điểm bắt đầu chung | R-04: check-in window, server ack, Late/Not confirmed rõ | US-05 | F-04 | FL-02 | T-12,T-14 |
| E-04: 7/12 thấy khác phòng suy yếu; interpretation chưa rõ | N-05 [I]: cảm giác cùng học với người quen | R-05 [P]: shared view nhẹ, không ép video | US-06 | F-05 | FL-02 | T-08,T-12,T-04,T-15 |
| H1 [P]: cần quan sát follow-through | N-06 [I]: ghi điều mình báo đã diễn ra | R-06: Completed/Left early/Unconfirmed self-report | US-07 | F-07 | FL-02 | T-13,T-15 |
| E-06: pressure/visibility concerns | N-07: riêng tư và tự nguyện | R-07: role access, minimal invite view, không public absence | US-08, US-03 | F-02,F-03,F-04,F-05,F-06,F-07,F-08 | FL-01, FL-02 | T-07,T-10,T-14,T-19 |
| Rủi ro plan thay đổi [I], không có finding survey riêng | N-08 [I]: tránh lời hẹn/reminder cũ | R-08: creator hủy trước start, đổi giờ bằng tạo mới | US-10 | F-08 | FL-01 | T-09,T-11,T-14 |

## Research và project work

T-01/02/03/04/15/16 kiểm tra assumptions, không giả làm MVP features. T-05/06/17/18/19/20 đáp ứng foundation, quality và submission. Không bắt mọi task quản trị phải có user story; requirement của assignment là căn cứ rõ.

E-05 dẫn tới Revise A5 và **không tạo task build public room**; đây là trace tới quyết định loại scope, không ép evidence thành feature. A3/H1 là cơ sở cho T-04/T-15/T-16. Không có feature ngoài MVP nào được gắn “đã validate” chỉ vì xuất hiện ở bảng so sánh.

## GitHub task index

| Task | Issue | Milestone | Status |
|---|---|---|---|
| T-01 | [#1](https://github.com/Lockin-4everyung/lockin-mobile/issues/1) | M1 | In Review |
| T-02 | [#2](https://github.com/Lockin-4everyung/lockin-mobile/issues/2) | M2 | Backlog |
| T-03 | [#3](https://github.com/Lockin-4everyung/lockin-mobile/issues/3) | M2 | Backlog |
| T-04 | [#4](https://github.com/Lockin-4everyung/lockin-mobile/issues/4) | M2 | Backlog |
| T-05 | [#5](https://github.com/Lockin-4everyung/lockin-mobile/issues/5) | M1 | In Review |
| T-06 | [#6](https://github.com/Lockin-4everyung/lockin-mobile/issues/6) | M1 | Backlog |
| T-07 | [#7](https://github.com/Lockin-4everyung/lockin-mobile/issues/7) | M2 | Backlog |
| T-08 | [#8](https://github.com/Lockin-4everyung/lockin-mobile/issues/8) | M2 | Backlog |
| T-09 | [#9](https://github.com/Lockin-4everyung/lockin-mobile/issues/9) | M3 | Backlog |
| T-10 | [#10](https://github.com/Lockin-4everyung/lockin-mobile/issues/10) | M3 | Backlog |
| T-11 | [#11](https://github.com/Lockin-4everyung/lockin-mobile/issues/11) | M3 | Backlog |
| T-12 | [#12](https://github.com/Lockin-4everyung/lockin-mobile/issues/12) | M3 | Backlog |
| T-13 | [#13](https://github.com/Lockin-4everyung/lockin-mobile/issues/13) | M3 | Backlog |
| T-14 | [#14](https://github.com/Lockin-4everyung/lockin-mobile/issues/14) | M3 | Backlog |
| T-15 | [#15](https://github.com/Lockin-4everyung/lockin-mobile/issues/15) | M4 | Backlog |
| T-16 | [#16](https://github.com/Lockin-4everyung/lockin-mobile/issues/16) | M4 | Backlog |
| T-17 | [#17](https://github.com/Lockin-4everyung/lockin-mobile/issues/17) | M1 | In Review |
| T-18 | [#18](https://github.com/Lockin-4everyung/lockin-mobile/issues/18) | M1 | In Review |
| T-19 | [#19](https://github.com/Lockin-4everyung/lockin-mobile/issues/19) | M1 | In Review |
| T-20 | [#20](https://github.com/Lockin-4everyung/lockin-mobile/issues/20) | M1 | Backlog |
