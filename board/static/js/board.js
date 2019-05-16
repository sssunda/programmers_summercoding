<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

    <script>
        function sort() {
            $(function () {
                $("#sortable").sortable();
                $("#sortable").disableSelection();
            });
        }

        function rank_change() {
            // 배열 생성
            var orderlist = $("#sortable").sortable("toArray");

            // 배열을 POST 로 넘김
            $.ajax({
                url: "{% url 'board:post_list_rank_update' %}",
                type: "POST",
                data: {
                    "orderlist": orderlist.toString(),
                    "csrfmiddlewaretoken": "{{csrf_token}}",
                },

                async: false,
                cache: false,
                success: function (data) {
                    if (data == "OK") {
                        alert("변경 내용이 저장되었습니다.");
                        window.location.reload(true); //현재화면 새로고침
                    }
                },
                error: function (request, status, error) {
                    alert("orderlist:" + orderlist + "\n" + "code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
                }


            })
        }

        $(document).ready(function () {
            $("#rank_btn").click(function () {
                if ($("#rank_btn").val() == "우선 순위 변경") {
                    sort()
                    $("#rank_btn").val('저장')
                    $("#post_add_btn").hide()
                    $("p").show()
                    $(".complete_btn").attr('disabled', true)
                }
                else {
                    rank_change()
                    $("#rank_btn").val('우선 순위 변경')
                    $("#post_add_btn").show()
                    $("p").hide()
                    $(".complete_btn").attr('disabled', false)
                }
            });
        });

        function complete_btn(id) {
            var url = "{% url 'board:complete' 'id' 'board:post_list' %}".replace("id", id)
            if (confirm('완료 처리하시겠습니까?')) {
                location.href = url
            }
        }

        function post_add_btn() {
            location.href = "{% url 'board:post_add' %}"
        }
    </script>