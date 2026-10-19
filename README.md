# LockIn - Assignment 1

LockIn nghiên cứu liệu lời hẹn tự học với bạn quen, có giờ rõ, RSVP và check-in, tạo đủ giá trị so với chat/lịch để người dùng chủ động quay lại.

**Bắt đầu tại [GitHub Wiki - Assignment 1](https://github.com/Lockin-4everyung/lockin-mobile/wiki).** [Bản nguồn trong repo](docs/wiki/Home.md) dựa trên ZIP mục 2.1–2.11, đã sửa mâu thuẫn, đối chiếu 12 phản hồi khảo sát và bổ sung 2.12, kế hoạch, traceability và checklist nộp bài.

| Điểm truy cập | Trạng thái ngày 19/10/2026 |
|---|---|
| [GitHub Organization](https://github.com/Lockin-4everyung) | Đã xác nhận tồn tại; chưa xác nhận toàn bộ thành viên |
| [Repository](https://github.com/Lockin-4everyung/lockin-mobile) | Public, chứa nguồn tài liệu và kế hoạch tiếp tục |
| [GitHub Wiki](https://github.com/Lockin-4everyung/lockin-mobile/wiki) | Home, 18 trang nội dung, 2 trang evidence tổng hợp và navigation |
| [GitHub Project - Board](https://github.com/orgs/Lockin-4everyung/projects/1/views/1) | 20 issue gắn 4 milestone; giữ 5 trạng thái do nhóm tạo |
| [GitHub Project - All Tasks](https://github.com/orgs/Lockin-4everyung/projects/1/views/2) | Table với Title, Assignees, Status, Milestone |
| [Evidence public](docs/research/survey-summary.md) | Tổng hợp ẩn danh từ 12 phản hồi; không chứa dữ liệu liên hệ |
| [Project plan](docs/wiki/13-Project-Foundation-Plan.md) | Backlog, role owner, dependencies và milestones; cần map thành viên thật |
| [Submission checklist](docs/wiki/15-Submission-Checklist.md) | Ghi rõ phần còn thiếu, không tuyên bố đã nộp |

Mobile là hướng để thử nghiệm. H1 về giá trị vượt công cụ hiện có vẫn **Investigate further**; chưa có interview/pilot, log dùng lại hoặc bằng chứng tăng hiệu quả học tập.

## Làm việc với bộ tài liệu

- Nguồn chuẩn: Markdown trong docs/wiki; research aggregate trong docs/research.
- Kiểm tra liên kết, ID, số liệu và backlog: python scripts/check_docs.py
- Xuất bộ Wiki để review/upload: python scripts/export_wiki.py
- Bộ xuất hiện tại: dist/wiki và dist/LockIn-Assignment1-Wiki.zip, đều local/ignored.
- [Hướng dẫn đưa lên GitHub](docs/PUBLISHING.md). Export chỉ tạo thư mục dist/wiki local; không push hoặc thay đổi GitHub.
- [Backlog CSV](planning/backlog.csv), [mốc công việc](planning/milestones.csv), [những sửa đổi](docs/REVIEW-NOTES.md).
- [Đối tượng GitHub đã tạo](planning/github/published-state.json): issue URL, milestone và Project item thật. Assignee được để trống theo yêu cầu người dùng; deadline chưa tự đặt.

Không cần triển khai app/backend hoặc làm UI hoàn chỉnh cho Assignment 1. Tài liệu phân biệt survey [S], nguồn chính thức [D], suy luận [I] và kế hoạch chưa chạy [P].
