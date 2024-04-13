$(function(){
//---------------------------------------------------------------------------
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];

    let h_data = "";
    for(let i=0; i<no.length; i++){
        h_data += "<tr id='"+no[i]+"'>";
        h_data += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
        h_data += "<td>"+no[i]+"</td>";
        h_data += "<td>"+name[i]+"</td>";
        h_data += "<td>"+kor[i]+"</td>";
        h_data += "<td>"+eng[i]+"</td>";
        h_data += "<td>"+math[i]+"</td>";
        h_data += "<td>"+total[i]+"</td>";
        h_data += "<td>"+avg[i]+"</td>";
        h_data += "<td>0</td>";
        h_data += "<td><button class='delBtn'>삭제</button></td>";
        h_data += "</tr>";
    }
    // 배열에 있는 데이터 추가
    $("#body").html(h_data);
//---------------------------------------------------------------------------
    // 입력버튼클릭
    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
    });
    // 팝업창에서 취소버튼
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    });
//---------------------------------------------------------------------------
    // 학생 입력버튼
    $("#confirmBtn").click(function(){

        if($("#name").val().length < 2){
            alert("이름을 입력하셔야 등록이 가능합니다.");
            $("#name").focus();
            return false;
        }
        else if($("#kor").val().length < 2){
            alert("국어점수를 입력하셔야 등록이 가능합니다.");
            $("#kor").focus();
            return false;
        }
        else if($("#eng").val().length < 2){
            alert("영어점수를 입력하셔야 등록이 가능합니다.");
            $("#eng").focus();
            return false;
        }
        else if($("#math").val().length < 2){
            alert("수학점수를 입력하셔야 등록이 가능합니다.");
            $("#math").focus();
            return false;
        }

        let my_no = Math.max.apply(null,no)+1;;
        no.push(my_no)
        let my_name = $("#name").val();
        let my_kor = Number($("#kor").val());
        let my_eng = Number($("#eng").val());
        let my_math = Number($("#math").val());
        let my_total = my_kor+my_eng+my_math;
        let my_avg = (my_total/3).toFixed(2);

        let h_data = "";

        h_data += "<tr id='"+my_no+"'>";
        h_data += "<td><input type='checkbox' name='stu' class='stuChk' value='"+my_no+"'></td>";
        h_data += "<td>"+my_no+"</td>";
        h_data += "<td>"+my_name+"</td>";
        h_data += "<td>"+my_kor+"</td>";
        h_data += "<td>"+my_eng+"</td>";
        h_data += "<td>"+my_math+"</td>";
        h_data += "<td>"+my_total+"</td>";
        h_data += "<td>"+my_avg+"</td>";
        h_data += "<td>0</td>";
        h_data += "<td><button class='delBtn'>삭제</button></td>";
        h_data += "</tr>";
        // html소스를 tbody 추가
        $("#body").append(h_data);

        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");

    }); // 하단입력버튼(팝업추가예정)
//---------------------------------------------------------------------------
    //table 삭제버튼 클릭
    $(".delBtn").click(function(){
        alert("test");
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    }); // table 삭제

    // (하단)체크된 학생 삭제
    $("#deleteBtn").click(function(){
        // 체크된 학생이 없을 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크해주셔야 가능합니다.");
            return false;
        }
        if(!confirm("정말 삭제하시겠습니까?")){
            return false;
        } // 삭제 if

        //모든 체크박스를 가져오기
        $(".stuChk").each(function(){
            //현재 체크박스가 체크가 되어 있는지 확인
            if($(this).is(":checked") == true ){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        }); // each

    }); // 체크된 학생 전체 삭제
//---------------------------------------------------------------------------
    // 전체선택
    $("#allChk").click(function(){  
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            });
        }
        else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
        }
    });// 전체선택
}); // 제이쿼리