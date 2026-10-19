# Assignment 1 review notes

Updated 19/10/2026. Nguồn là ZIP người dùng cung cấp và assignment-1-req.txt. Nội dung ZIP là bản nháp để kiểm tra; chỉ dẫn “exclude 2.12/Submission” trong ZIP không thay yêu cầu người dùng hiện tại.

## Sửa nội dung

- Repo public trống khi clone; tạo bộ tài liệu discovery, không tự triển khai app ngoài scope Assignment 1.
- Đối chiếu native response Sheet: 12 rows; các số chính khớp. Thay mô tả “đã có file XLSX” bằng provenance thực; không đọc contact AD hoặc lưu raw responses.
- A6 trong registry là privacy nhưng decision cũ nói notifications: giữ A6 đúng nghĩa, thêm A8 riêng và nối evidence/story/task.
- A1 nói frequency nhưng survey chủ yếu hỏi incident và hồi tưởng tuần: hạ kết luận thành Investigate further, giữ problem để nghiên cứu.
- Q12 có thể hiểu phòng vật lý/online; shared participant view là hypothesis, chưa là giải pháp chứng minh.
- Không auto no-show/Completed từ absence/timer/AppState. Phân biệt Not confirmed, Late confirmed và outcome tự báo.
- Bổ sung expired/pending invite, identity/onboarding, cancellation, offline/retry và rule timezone thống nhất giữa stories/flows.
- Bổ sung US-09 lịch quay lại và US-10 hủy trước start như enablers của core path; không mở rộng public room/chat/video/blocking.
- Evidence plan có screening, baseline, sample unit, operational definitions và support/challenge/unresolved trước pilot; chưa có kết quả pilot.
- Canvas vẫn đúng 3×3 đề bài; metrics/advantage/revenue có nhãn hypothesis; effort có đơn vị và capacity chưa xác nhận.

## Bổ sung yêu cầu thiếu

- Home/README: điều hướng theo toàn bộ rubric, evidence accessible dưới dạng anonymous aggregate.
- 2.12: organization đã tồn tại, role mapping cần người thật, workflow, backlog 20 task và 4 milestones.
- Traceability đầy đủ tới development/validation task thay đoạn ZIP hoãn cho người khác.
- Checklist publication/submission; nguồn Wiki xuất được sang repository .wiki.git riêng.
- CSV backlog/milestones, issue template; local checker cho links, IDs và aggregate.

## Chưa thể tự xác nhận

Roster/GitHub username, membership toàn nhóm, kênh tuyển survey cũ, deadline/capacity, team sign-off, Project URL thật và quyền publish. Tài khoản CLI đọc được repo nhưng push=false; Project query thiếu read:project. Không sửa quyền/auth, không tạo board/issue, không push/submit trong phiên này.

Người dùng xác nhận ngày 19/10/2026: chưa có GitHub Project và survey thực hiện qua Google Forms. Link Form đã có trong ZIP và được giữ trong References; Google Forms là phương pháp, chưa cho biết nhóm/lớp/nơi phát link.

Sau đó người dùng cung cấp Project https://github.com/orgs/Lockin-4everyung/projects/1/views/1 và yêu cầu làm bước 5–8, để phân công sau. API xác nhận Project public, title LockIn - Product Development, hiện chưa có items. Giữ nhãn Status người dùng đã tạo: Backlog, Todo, In Progress, In Review, Done. Đã chuẩn bị 4 milestone payloads và 20 issue bodies trong planning/github; chưa tạo đối tượng GitHub. Lệnh tạo M1 bị GitHub trả HTTP 404, phù hợp trạng thái tài khoản CLI GSlay có push=false; GraphQL trả INSUFFICIENT_SCOPES cho read:project. Cần xác thực tài khoản có quyền phù hợp trước khi publish.

Phỏng vấn, benchmark và pilot chưa thực hiện. Tài liệu nêu thẳng limitation; không tạo số liệu, người tham gia, sự đồng ý hay nhiệm vụ Done giả.

## Publication update - 19/10/2026

Đã xác thực DucMinh2211 với quyền ADMIN repo và quyền sửa Project. Đã tạo 4 milestone, 20 issue có acceptance/dependencies/traceability, liên kết Project với lockin-mobile và thêm All Tasks table. Giữ Board và Status của người dùng. Repo và Wiki được xuất bản; T-17 chuyển In Review để nhóm kiểm tra. Assignee để trống theo yêu cầu, không tự đặt deadline và không đánh dấu nghiên cứu/build tương lai Done. Các đoạn về thiếu quyền/Project chưa có phía trên là lịch sử trước khi xác thực và xuất bản.
