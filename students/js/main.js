$(function(){
    let s_count=1;
    // 1. ajax stu_score.json 10개 데이터를 출력하시오.
     // 최초 데이터 불러오기
    $.ajax({
        url:"http://127.0.0.1:5500/students/json/stu_score.json",
        data:{},
        type:"get",
        dataType:"json",
        success:function(data){
            alert("데이터 로드 성공");
            s_count = data.length;
            let htmldata = "";
            for(let i=0; i<10; i++){
                htmldata += "<tr id='"+data[i].no+"'>";
                htmldata += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                htmldata += "<td>"+data[i].no+"</td>";
                htmldata += "<td>"+data[i].name+"</td>";
                htmldata += "<td>"+data[i].kor+"</td>";
                htmldata += "<td>"+data[i].eng+"</td>";
                htmldata += "<td>"+data[i].math+"</td>";
                htmldata += "<td>"+data[i].total+"</td>";
                htmldata += "<td>"+data[i].avg+"</td>";
                htmldata += "<td>"+data[i].rank+"</td>";
                htmldata += "<td><button class='delBtn'>삭제</button></td>";
                htmldata += "</tr>";
            }

            $("#body").html(htmldata)
        },
        error:function(){alert("로드 에러");}

    }); // ajax
    // 2. 학생입력 -> 학생 추가 프로그램을 구성하시오.
    $("#writeBtn").click(function(){
        if($(".stuChk:checked").length>=1){
            alert("학생입력을 하시려면 체크를 해제하셔야 가능합니다. \n 자동 체크해체 합니다.");
            // 체크모두 해제
            $(".stuChk").each(function(){
                $("#allChk").prop("checked",false);
                $(this).prop("checked",false);
            });
            return false;

        }
        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);
    });
    // 취소버튼
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        // 초기화
        $("#id").val("");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    });

    $("#confirmBtn").click(function(){
        if($("#id").val()==""){

            if($("#name").val().length < 2){
                alert("이름을 입력하셔야 등록이 가능합니다.");
                $("#name").focus();
                return false;
            }

            s_count = s_count+1;
            let i_name = $("#name").val();
            let i_kor = Number($("#kor").val());
            let i_eng = Number($("#eng").val());
            let i_math = Number($("#math").val());
            let i_total = i_kor + i_eng + i_math;
            let i_avg = (i_total/3).toFixed(2);

            let htmlData = "";

            htmlData += "<tr id='"+s_count+"'>";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+s_count+"'></td>";
            htmlData += "<td>"+s_count+"</td>";
            htmlData += "<td>"+i_name+"</td>";
            htmlData += "<td>"+i_kor+"</td>";
            htmlData += "<td>"+i_eng+"</td>";
            htmlData += "<td>"+i_math+"</td>";
            htmlData += "<td>"+i_total+"</td>";
            htmlData += "<td>"+i_avg+"</td>";
            htmlData += "<td>0</t3d>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += "</tr>";

            $("#body").append(htmlData);

            // input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
        }
        // 3. 학생수정 -> 학생성적수정이 가능하게 구성하시오.
        else{
            o_no = $("#id").val();
            o_name = $("#name").val();
            o_kor = Number($("#kor").val());
            o_eng = Number($("#eng").val());
            o_math = Number($("#math").val());
            let o_total = o_kor + o_eng + o_math;
            let o_avg = (o_total/3).toFixed(2);

            let htmlData = "";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+o_no+"'></td>";
            htmlData += "<td>"+o_no+"</td>";
            htmlData += "<td>"+o_name+"</td>";
            htmlData += "<td>"+o_kor+"</td>";
            htmlData += "<td>"+o_eng+"</td>";
            htmlData += "<td>"+o_math+"</td>";
            htmlData += "<td>"+o_total+"</td>";
            htmlData += "<td>"+o_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";

            $("#"+o_no).html(htmlData);

            // input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
        }
    }); // 입력 수정
    $("#modifyBtn").click(function(){
        if($(".stuChk:checked").length != 1){
            alert("학생 1명만 선택하셔야 수정이 가능합니다.");
            return false;
        }
        o_id = $(".stuChk:checked").parent();
        o_no = o_id.next().text();
        o_name = o_id.next().next().text();
        o_kor = o_id.next().next().next().text();
        o_eng = o_id.next().next().next().next().text();
        o_math = o_id.next().next().next().next().next().text();

        $(".p_all").css("display","block");
        $("#name").prop("readonly",true);
        
        $(".p_main h2").text("학생성적수정");
        $("#id").val(o_no);
        $("#name").val(o_name);
        $("#kor").val(o_kor);
        $("#eng").val(o_eng);
        $("#math").val(o_math);
    });

    // 4. 학생삭제 -> 선택된 학생이 삭제 되도록 구성하시오.
    $(document).on("click",".delBtn",function(){
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });
    // 전체 선택
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            });
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
        }
    }); // 전체 선택

    $("#deleteBtn").click(function(){
        // 체크되어 있는 것이 없을 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 가능합니다.");
            return false;
        }
        if(!confirm("정말 삭제하시겠습니까?")){
            return false;
        }
        // 체크 되어있는 학생 모두 삭제
        $(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        }); //each
    });



}) // 제이쿼리