# Product Rules & Metrics

> 19/10/2026 · Quy tắc đề xuất [I/P], cần review và thử trước implementation.

## Thời gian và lifecycle

Lưu instant UTC với timezone hiển thị; không so chuỗi giờ địa phương. Start phải ở tương lai, end > start; trước mắt không recurring session. Creator + 1–3 invitee, tối đa 4 người.

Commitment: Scheduled → Active khi đến start → Ended khi đến end; creator có thể Cancelled trước start. MVP không sửa giờ tại chỗ: hủy và tạo mới, không kế thừa RSVP cũ. Active không hủy toàn nhóm; từng người có thể tự Left early sau check-in.

Creator có Accepted membership khi tạo nhưng attendance chưa xác nhận. Invitee Pending → Accepted/Declined trước start; Pending hết hạn ở start thành Expired. RSVP không tự biến thành check-in. Declined/Expired không được tính participant-session đã nhận lời trong attendance denominator.

Check-in mở **[start − 5 phút, end)**. Server-received time ≤ start + 5 phút là On-time confirmed; sau đó đến trước end là Late confirmed. Không có server-acknowledged check-in lúc end là **Not confirmed**. Nhãn này không chứng minh vắng học hay vi phạm.

Accepted participant đã check-in có thể chọn Left early trước end. Từ end, có thể tự báo Completed; không chọn là Unconfirmed outcome. Giữ attendance record và outcome riêng; một Late participant vẫn có thể báo Completed. Không tự sinh Completed khi timer hết. Outcome gửi muộn ghi đúng thời điểm báo, không sửa attendance time.

## Các tình huống biên

- Retry cùng request không tạo phiên/RSVP/check-in thứ hai. Chưa server acknowledge thì hiển thị pending, không “đã lưu”.
- Offline có thể xem lịch cache có nhãn chưa cập nhật; gửi lại check-in chỉ khi server còn trong window. Không backdate bằng đồng hồ máy; có thể ghi chú mất mạng riêng trong pilot.
- Reminder đề xuất 10 phút trước start; nếu Accept sau mốc này, hiển thị lịch/in-app thay vì hứa giao reminder đã qua. Hủy phải vô hiệu nhắc cũ; nếu nhắc cũ đã hiện, khi mở phải thấy Cancelled.
- Không có quyền notification vẫn xem lịch/check-in. Invite chia sẻ bằng chat/link, remote push không là dependency bắt buộc.
- Background, tắt màn hình, đọc PDF, mở calculator hay code không tự đổi outcome. Roster hiển thị bản ghi check-in, không gọi đó là “đang tập trung trực tiếp”.

## Visibility

| Người | Được thấy/làm |
|---|---|
| Creator | Xem responses lời mời và roster/outcome, hủy trước start; không sửa outcome người khác |
| Pending invitee đã xác thực | Inviter, giờ/mục đích tối thiểu và policy; Accept/Decline trước start; chưa xem roster/outcome |
| Accepted member | Xem roster/check-in/outcome trong commitment, tự check-in/report; không sửa người khác |
| Declined/Expired | Xác nhận response của mình nếu cần, không có quyền xem session/roster/outcomes |
| Người ngoài hoặc người mở link sai identity | Không xem private details; lỗi chung, không lộ danh sách thành viên |

Không public history/leaderboard về vắng/bỏ sớm. Chỉ thu identity tối thiểu; không import contacts/social graph/camera/chat. Cách login/invite capability cụ thể còn T-07; permission rules phải kiểm được trước pilot T-14.

## Metric dictionary

| Metric | Numerator / denominator hoặc cách đo | Giới hạn |
|---|---|---|
| Create / RSVP active time | Active thao tác creator + invitee từ task start đến xác nhận | Ghi waiting time riêng |
| Invite-to-RSVP elapsed | Thời gian từ giao lời mời hợp lệ tới response đầu tiên | Báo chưa trả lời như censored/missing, không gán bằng 0 |
| RSVP rate | Accept + Decline trước start / valid delivered invite | Không gọi Decline là adoption thành công |
| On-time confirmed rate | Participant-sessions check-in đúng window on-time / Accepted, không cancelled | Không đo việc học thật; báo missing/offline |
| Outcome report rate | Accepted participant-sessions có self-report / Accepted, không cancelled | Tách Completed, Left early và Unconfirmed; không đồng nghĩa hiệu quả |
| Repeat pair rate | Cặp tự tạo và có người Accept phiên LockIn mới trong 7 ngày / đủ 4 cặp pilot | Không trộn pair với person |
| Burden / pressure | Sau mỗi điều kiện hỏi có tăng thao tác/áp lực và lý do | Preference bổ sung cho behavioral evidence |

Logging tối thiểu: ID giả danh, session ID, condition baseline/LockIn, thời gian chuẩn server, event type và kết quả retry. Không thu nội dung riêng hoặc app đang mở. Thresholds [Evidence Plan](04-Evidence-Plan.md) phải được chốt trước thu dữ liệu; bảng này chưa có số kết quả pilot.
