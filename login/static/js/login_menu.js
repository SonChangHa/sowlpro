document.querySelector('#loginId').focus();
document.getElementsByClassName('btn_login')[0].addEventListener('click',(e)=>{
    if(document.querySelector('#loginId').value == ""){
        alert('아이디를 입력해주세요!');
        e.preventDefault();
        document.querySelector('#loginId').focus();
        return;
    }
    if(document.querySelector('#loginPw').value == ""){
        alert('비밀번호를 입력해주세요!');
        e.preventDefault();
        document.querySelector('#loginPw').focus();
        return;
    }
})