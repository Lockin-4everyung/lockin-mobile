# 2.12. Project Foundation & Project Plan

> 20/10/2026 · Đã xác nhận 4 thành viên, phân công research/design/GitHub setup và link Figma.

## Foundation được kiểm tra

| Hạng mục | Trạng thái có bằng chứng | Còn cần |
|---|---|---|
| [Organization Lockin-4everyung](https://github.com/Lockin-4everyung) | Tồn tại, loại Organization qua GitHub API | Roster và xác nhận membership của mọi người |
| [Repository lockin-mobile](https://github.com/Lockin-4everyung/lockin-mobile) | Public, có nguồn tài liệu và backlog | Team review nội dung và cập nhật khi có evidence mới |
| Thành viên | Nhóm cung cấp 4 người; API xác nhận cả DucMinh2211, Hungg101, huynguyen1234567890, minhphan-hcmut đã join | Membership đủ 4/4 theo roster được cung cấp ngày 20/10/2026 |
| [GitHub Project #1](https://github.com/orgs/Lockin-4everyung/projects/1/views/1) | Public; 20 issue, 4 milestone, Board và All Tasks table | Đã gán 13 task phù hợp với trách nhiệm; 7 task code/QA phần mềm chưa chốt người |
| [Wiki](https://github.com/Lockin-4everyung/lockin-mobile/wiki) | Bộ tài liệu có navigation và evidence tổng hợp | Team review và giữ đồng bộ với nguồn repo |
| Quyền quản lý | Đã xác thực DucMinh2211 có quyền ADMIN repo và quyền cập nhật Project | Các thành viên khác cần quyền phù hợp để cộng tác |

Không tạo organization trùng vì organization đã tồn tại. Không giả danh thành viên hoặc tự đánh dấu tất cả đã join.

## Ownership và cách cập nhật

Phân công do người dùng xác nhận ngày 20/10/2026. Github username đã được đối chiếu với thành viên organization.

| Thành viên | GitHub | Trách nhiệm đã chốt |
|---|---|---|
| Huy Nguyễn | [huynguyen1234567890](https://github.com/huynguyen1234567890) | Phân tích số liệu khảo sát, hỗ trợ nghiên cứu |
| Minh Phan | [minhphan-hcmut](https://github.com/minhphan-hcmut) | Repository, Organization, GitHub Project và tài liệu setup |
| Hùng | [Hungg101](https://github.com/Hungg101) | Thiết kế/prototype Figma |
| Đức Minh | [DucMinh2211](https://github.com/DucMinh2211) | Team lead, tạo Google Form, research và điều phối/review sản phẩm |

[Figma - LockIn](https://www.figma.com/design/toEag0gceMnBkZudr5Yej0/LockIn) do Hùng phụ trách. Link được nhóm cung cấp; nội dung file chưa được kiểm tra qua công cụ, nên không dùng sự tồn tại của link để kết luận prototype hoàn thành. Figma hỗ trợ T-08 và hai critical flows.

Mỗi task đã gán có một người chủ trì; các task research/đối chiếu số liệu có thể có người hỗ trợ. Product/research lead là Đức Minh, phân tích số liệu là Huy, Design là Hùng, Coordinator cho GitHub setup là Minh Phan. Task T-20 do lead điều phối, deadline/người thực hiện thao tác nộp vẫn do nhóm chốt.

Mobile implementation, backend/data-sync và software QA chưa được phân công: T-07, T-09, T-10, T-11, T-12, T-13, T-14 giữ Assignee trống. Không tự chuyển Huy sang backend chỉ vì phụ trách phân tích dữ liệu khảo sát. Khi kéo các task này vào To Do, nhóm cần chốt người chịu trách nhiệm.

## Workflow và quality gate

**Backlog → To Do → In Progress → Review → Done.** Project thực tế dùng nhãn Todo cho To Do và In Review cho Review; giữ các nhãn người dùng đã tạo. Blocked là cờ + lý do/dependency, không che tiến độ bằng Done.

To Do: mục tiêu/acceptance rõ, owner thật, evidence/story trace, dependency và milestone. Review: có artifact/link và validation thực. Done: reviewer xác nhận artifact đạt acceptance; research inconclusive vẫn có thể Done nếu thu thập/phân tích đúng và decision ghi rõ. Không tạo task giả hoặc coi “có template” là đã interview.

## Milestones đề xuất [P]

Tuần tính tương đối từ lúc nhóm chốt kế hoạch, không phải deadline môn học đã được xác nhận.

| ID | Thời gian đề xuất | Outcome và exit criteria |
|---|---|---|
| M1 Assignment 1 foundation | Trước ngày nộp thật (chưa cung cấp) | Tài liệu review; roster/owners; public Wiki/Project; links và evidence accessible |
| M2 Discovery follow-up & design | Tuần 1–2 sau M1 | Phỏng vấn và task test có consent; revised H1 decision; flows/prototype; scope/capacity được chốt |
| M3 Core mobile pilot build | Tuần 3–4 | Create/invite/RSVP/check-in/outcome end-to-end; local reminder; access/sync đúng; test thiết bị mục tiêu |
| M4 Pilot & product decision | Tuần 5–6 + 7 ngày quan sát repeat | 4 cặp nếu tuyển đủ; dataset thiếu được ghi; kết quả theo protocol; Keep/Revise/Reject/Investigate further có lý do |

Không khóa M3 trước khi T-07 xác minh identity/invite feasibility và T-04 chỉ ra friction. Có thể thử prototype trước build. Nếu M2 bác H1, sửa milestones/scope và decision log.

## Backlog thực, dẫn xuất từ MVP

Status dưới đây đồng bộ với GitHub Project. Review trong bảng tương ứng In Review trên board, nghĩa là artifact đã có và đang chờ review; không có nghĩa đã được nhóm duyệt. Các issue thật được liên kết ở cột GitHub issue. CSV nguồn: planning/backlog.csv.

| Task | Việc cần làm / outcome | Role owner | Milestone | Depends | Status | GitHub issue | Chủ trì | Hỗ trợ |
|---|---|---|---|---|---|---|---|---|
| T-01 | Đối chiếu survey, sửa evidence và limitations | Research | M1 | - | Review | [#1](https://github.com/Lockin-4everyung/lockin-mobile/issues/1) | huynguyen1234567890 | - |
| T-02 | Xác nhận recruitment cũ; tuyển mẫu/consent follow-up | Research | M2 | T-06 | Backlog | [#2](https://github.com/Lockin-4everyung/lockin-mobile/issues/2) | DucMinh2211 | - |
| T-03 | 4–6 critical-incident interviews, ghi cả contradiction | Research | M2 | T-02 | Backlog | [#3](https://github.com/Lockin-4everyung/lockin-mobile/issues/3) | DucMinh2211 | huynguyen1234567890 |
| T-04 | Task comparison 6 người baseline/prototype | Research | M2 | T-03,T-08 | Backlog | [#4](https://github.com/Lockin-4everyung/lockin-mobile/issues/4) | DucMinh2211 | huynguyen1234567890 |
| T-05 | Review direction, assumptions, scope và canvas | Product | M1 | T-01 | Review | [#5](https://github.com/Lockin-4everyung/lockin-mobile/issues/5) | DucMinh2211 | - |
| T-06 | Xác nhận roster/membership, owner thật, Project public | Coordinator | M1 | - | Backlog | [#6](https://github.com/Lockin-4everyung/lockin-mobile/issues/6) | minhphan-hcmut | - |
| T-07 | Spike identity/invite, target device và sync feasibility | Mobile | M2 | T-05 | Backlog | [#7](https://github.com/Lockin-4everyung/lockin-mobile/issues/7) | Chưa phân công | - |
| T-08 | Prototype hai flows, test logic/time/privacy nội bộ | Product | M2 | T-05,T-07 | Backlog | [#8](https://github.com/Lockin-4everyung/lockin-mobile/issues/8) | Hungg101 | - |
| T-09 | Lịch/tạo commitment, validation timezone và hủy | Mobile | M3 | T-04,T-07 | Backlog | [#9](https://github.com/Lockin-4everyung/lockin-mobile/issues/9) | Chưa phân công | - |
| T-10 | Identity, invite và RSVP an toàn, retry không trùng | Data | M3 | T-07,T-09 | Backlog | [#10](https://github.com/Lockin-4everyung/lockin-mobile/issues/10) | Chưa phân công | - |
| T-11 | Local reminder, opt-out và fallback lịch | Mobile | M3 | T-09,T-10 | Backlog | [#11](https://github.com/Lockin-4everyung/lockin-mobile/issues/11) | Chưa phân công | - |
| T-12 | Check-in + shared participant view, server ack | Data | M3 | T-10 | Backlog | [#12](https://github.com/Lockin-4everyung/lockin-mobile/issues/12) | Chưa phân công | - |
| T-13 | Outcome tự báo và lịch sử cá nhân | Data | M3 | T-12 | Backlog | [#13](https://github.com/Lockin-4everyung/lockin-mobile/issues/13) | Chưa phân công | - |
| T-14 | Test access, offline, retry, timezone và cancellation | QA | M3 | T-09,T-10,T-11,T-12,T-13 | Backlog | [#14](https://github.com/Lockin-4everyung/lockin-mobile/issues/14) | Chưa phân công | - |
| T-15 | Chạy pilot/quan sát repeat; ghi missing data | Research | M4 | T-02,T-04,T-14 | Backlog | [#15](https://github.com/Lockin-4everyung/lockin-mobile/issues/15) | DucMinh2211 | huynguyen1234567890 |
| T-16 | Đánh giá H1 và A1–A8, cập nhật scope/decision | Product | M4 | T-15 | Backlog | [#16](https://github.com/Lockin-4everyung/lockin-mobile/issues/16) | DucMinh2211 | huynguyen1234567890 |
| T-17 | Publish tài liệu/Wiki và thêm tasks thật vào Project | Coordinator | M1 | T-05,T-06,T-19 | Review | [#17](https://github.com/Lockin-4everyung/lockin-mobile/issues/17) | minhphan-hcmut | - |
| T-18 | Kiểm tra artifact, links, traceability và Mermaid | QA | M1 | T-01,T-05 | Review | [#18](https://github.com/Lockin-4everyung/lockin-mobile/issues/18) | minhphan-hcmut | huynguyen1234567890 |
| T-19 | Chốt protocol/ngưỡng, metrics và visibility policy | Research | M1 | T-05 | Review | [#19](https://github.com/Lockin-4everyung/lockin-mobile/issues/19) | DucMinh2211 | huynguyen1234567890 |
| T-20 | Kiểm tra public entry và nộp đúng hạn môn học | Coordinator | M1 | T-17,T-18,T-19 | Backlog | [#20](https://github.com/Lockin-4everyung/lockin-mobile/issues/20) | DucMinh2211 | - |

Acceptance cụ thể, story/feature/flow và dependencies của từng task có trong CSV; không tự đổi thành Done. T-03/04/15/16 là việc nghiên cứu tiếp theo, không bị mô tả đã làm để lấp bài.

## Capacity, risks và progress

Estimate development F-01–F-08 = 22 person-day; cộng 4 thiết kế + 5 QA + 4 analysis/review = **35 person-day** sơ bộ, chưa gồm overhead tuyển mẫu/chờ pilot. Capacity thật = tổng ngày mỗi người cam kết sau khi trừ môn khác/overlap role. Chưa có dữ liệu này nên feasibility còn cần xác nhận. Ưu tiên một platform thử nghiệm phù hợp thiết bị tuyển được; quyết định Android/iOS chưa chốt.

Nếu capacity thiếu: giảm số platform, bỏ remote push/deep link nâng cao, dùng prototype cho H1 trước. Không bỏ privacy, RSVP hoặc outcome đến mức core path không còn test được. Rủi ro lớn nhất là adoption yếu, không phải thiếu feature.

Tiến độ ngày 20/10/2026: 20 issue, 5 In Review (T-01/05/17/18/19), 15 Backlog, 0 Done. Đã có 13 task được gán chủ trì theo phân công mới; 7 task code/QA phần mềm còn trống. Cập nhật người phụ trách không tự thay đổi trạng thái hoàn thành hoặc xác nhận nghiên cứu đã thực hiện.

## Milestone GitHub

- [M1 - Assignment 1 Foundation](https://github.com/Lockin-4everyung/lockin-mobile/milestone/1)
- [M2 - Discovery Follow-up and Design](https://github.com/Lockin-4everyung/lockin-mobile/milestone/2)
- [M3 - Core Mobile MVP](https://github.com/Lockin-4everyung/lockin-mobile/milestone/3)
- [M4 - Pilot and Product Decision](https://github.com/Lockin-4everyung/lockin-mobile/milestone/4)
