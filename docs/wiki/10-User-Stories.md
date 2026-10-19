# 2.10. User Stories

> 19/10/2026 · Story mô tả user value; acceptance criteria là đề xuất cho thiết kế, chưa phải test đã pass.

| ID | User story | Requirement / Feature | Acceptance criteria |
|---|---|---|---|
| US-01 | As a student, I want to set a study commitment with clear start and end times, so that everyone knows when to begin and finish. | R-01 / F-01 | Start ở tương lai, end sau start; lưu một thời điểm thống nhất, hiển thị timezone địa phương; lỗi lưu không tạo phiên trùng |
| US-02 | As a student, I want to invite specific friends and see their responses, so that I know who plans to study with me. | R-02 / F-02/F-03 | Mời 1–3 người xác định; creator tự Accepted nhưng chưa check-in; có trạng thái Pending/Accepted/Declined/Expired |
| US-03 | As an invited student, I want to respond with minimal effort, so that joining is no harder than replying in chat. | R-02/R-07 / F-02/F-03 | Identity được kiểm tra; giữ đúng lời mời qua onboarding; Accept/Decline rõ; invalid/expired/wrong-user có hướng xử lý; đo active task time |
| US-04 | As a committed student, I want an optional reminder, so that I remember the session I agreed to join. | R-03 / F-06 | Xin quyền đúng ngữ cảnh; nhắc mặc định đề xuất 10 phút trước start nếu còn kịp; tắt được; lịch vẫn dùng khi từ chối quyền |
| US-05 | As a participant, I want to check in and see confirmed check-ins, so that we have a clear shared starting point. | R-04 / F-04 | Chỉ Accepted member, trong [start − 5 phút, end); phân biệt on-time/late; chưa sync không hiện thành công; retry không tạo trùng |
| US-06 | As a student, I want a lightweight session with familiar participants, so that I can feel accompanied without camera or voice. | R-05 / F-05 | Timer từ thời gian phiên; hiển thị check-in chứ không tuyên bố người đang nhìn màn hình; quay lại app không làm mất phiên |
| US-07 | As a participant, I want to report completion or an early departure, so that my history reflects what I reported happened. | R-06 / F-07 | Left early sau check-in và trước end; Completed từ end; không báo = Unconfirmed; nhãn self-report và lưu thời điểm |
| US-08 | As a student, I want clear control over who can see my commitment, so that I can participate without public pressure. | R-07 / F-02–F-08 | Pending chỉ thấy thông tin tối thiểu; roster/outcome chỉ creator + Accepted; Declined/Expired/người ngoài bị từ chối; giải thích visibility trước Accept |
| US-09 | As a student, I want to find my upcoming and recent commitments, so that I can return even if I miss a notification. | R-01/R-03 / F-01/F-06/F-07 | Phân biệt upcoming/ended/cancelled; lịch vẫn mở không cần push; cache có nhãn cũ khi offline; không tự xác nhận tham gia |
| US-10 | As an organiser, I want to cancel a session before it starts, so that friends do not follow an outdated plan. | R-08 / F-08 | Chỉ creator trước start; xác nhận hủy; tất cả thấy Cancelled sau sync; vô hiệu lời mời/reminder; đổi giờ bằng hủy và tạo lại |

Check-in không đo hiệu quả học tập. Những tiêu chí về thời gian/quyền dùng chung ở [Product Rules](17-Product-Rules-Metrics.md).

## Traceability

Nguồn và user needs có ID tại [Evidence Register](16-Evidence-Register.md). Bảng đủ chuỗi ở [Traceability Matrix](14-Traceability-Matrix.md); mỗi story nối đến requirement, feature, flow và development task. Hypothesis/inference được ghi riêng, không biến thành survey finding.
