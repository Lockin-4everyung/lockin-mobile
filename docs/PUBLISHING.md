# Publish the prepared Assignment 1 documentation

Bản chuẩn nằm ở docs/wiki và docs/research. Thư mục docs/wiki trong source repository chưa tự trở thành GitHub Wiki.

## Chuẩn bị và kiểm tra local

Chạy từ repository root:

~~~powershell
python scripts/check_docs.py
python scripts/export_wiki.py
~~~

Exporter ghi bộ Wiki tự chứa vào dist/wiki và dist/LockIn-Assignment1-Wiki.zip, đổi local links cho đúng vị trí, kèm Home, _Sidebar, _Footer và research aggregates. Không thực hiện network, commit hoặc push. dist được gitignore.

Kiểm tra cú pháp Mermaid tùy chọn (Node.js; dependencies chỉ ở cache ignored):

~~~powershell
npm install --prefix .cache/docs-tools --no-audit --no-fund --ignore-scripts mermaid@11.17.2 jsdom@26.1.0
node scripts/check_mermaid.mjs
~~~

Parser check không thay visual review sơ đồ trên GitHub sau publish.

## Source repository

Người có quyền write review toàn bộ diff, xác nhận owners/membership/deadline, rồi commit/push bằng workflow của nhóm. Không dùng dữ liệu identity của người khác để commit. README/Home phải cập nhật URL Project thật sau khi xác minh.

## GitHub Wiki

Theo [GitHub Docs](https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages), tạo một trang Wiki ban đầu bằng tài khoản có write nếu Wiki chưa được khởi tạo, sau đó clone wiki repository riêng.

~~~powershell
git clone https://github.com/Lockin-4everyung/lockin-mobile.wiki.git ..\lockin-mobile-wiki
Copy-Item -Path .\dist\wiki\* -Destination ..\lockin-mobile-wiki -Recurse -Force
~~~

Repo và Wiki đã được xuất bản ngày 19/10/2026 theo yêu cầu người dùng. Các lệnh trên là quy trình cập nhật tiếp theo: kiểm tra đúng remote và diff trước commit/push, giữ nguyên những trang khác nếu có. Nội dung được push lên default branch của wiki repository mới hiển thị live.

## GitHub Project

1. Dùng Project của organization nếu đã có; không tạo duplicate. Xác minh URL và quyền public/read của người chấm.
2. Field Status: Backlog, To Do, In Progress, Review, Done; thêm Milestone, Assignee, Role, Task ID, Story/Feature/Flow, Dependencies.
3. Dùng planning/backlog.csv làm input tạo issue/draft item qua UI hoặc công cụ được nhóm chọn; CSV không phải board và không hứa GitHub tự import mọi field.
4. Đã có 4 milestone và 20 issue trong Project #1. Người dùng yêu cầu để Assignee trống và phân công sau; khi chốt người phụ trách, dùng username thật thay role. Giữ đúng trạng thái evidence/artifact; chưa làm thì không Done.
5. Lưu issue number/URL và Project item vào task mapping sau khi tạo, cập nhật docs/README.
6. Board/Table theo status/assignee, Roadmap theo milestone; báo progress dựa trên outcome và blocked dependencies.

## Trước nộp

Mở public entry point không đăng nhập; đi tới Wiki Home, organization, Project và anonymous summary. Render được hai Mermaid flows, không có local filesystem links hoặc raw contact data. Hoàn tất [checklist](wiki/15-Submission-Checklist.md) và chỉ một người nộp cho nhóm theo deadline môn học thật.
