function display(){
    // get the content of input
    let cmt = document.getElementById("comment").value,
        contact = document.getElementById("User_contact").value,
        feedback = document.getElementById("view");
    if ((cmt !=="" && cmt !== null) && (contact !=="" && contact !== null)) {
        //feedback
        feedback.innerHTML = "<button type=\"button\" onclick=\"feedback()\" class=\"col-2  offset-10 btn btn-primary btn-dark\">提交的留言</button>"
    }
    else {
        alert("请输入留言和昵称")
    }
}

function feedback(){

    let contact = document.getElementById("User_contact").value,
        cmt = document.getElementById("comment").value,
        content = contact+"说："+cmt;
    alert(content);
}
