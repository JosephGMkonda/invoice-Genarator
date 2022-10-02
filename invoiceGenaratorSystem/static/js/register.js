const usernameField = document.querySelector("#usernameField")
const feedBackArea = document.querySelector('.invalid-feedback') 
const emailField = document.querySelector('#emailField')
const emailFeedBackArea = document.querySelector('.emailFeedBackArea')
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput')
const emailSuccessOutput = document.querySelector('.emailSuccessOutput')
const showPasswordToggle = document.querySelector('.showPasswordToggle')
const passwordField = document.querySelector('#passwordField')
const submitBtn = document.querySelector('.submit-btn')
const firstnameField = document.querySelector('#firstnameField')
const firstnameSuccessOutput = document.querySelector('.firstnameSuccessOutput')
const lastnameField = document.querySelector('#lastnameField')
const lastnameSuccessOutput = document.querySelector('.lastnameSuccessOutput')


const handleToggleInput = (e) => {
    if(showPasswordToggle.textContent=="SHOW"){
        showPasswordToggle.textContent="HIDE";
        passwordField.setAttribute("type","password");



    }
    else{
        showPasswordToggle.textContent="SHOW";
        passwordField.setAttribute("type","text");

    }


}

showPasswordToggle.addEventListener('click',handleToggleInput)


emailField.addEventListener("keyup" ,(e) => {

    const emailVal = e.target.value;
    emailSuccessOutput.textContent =`Chencking ${emailVal}`
    emailField.classList.remove('is-invalid')
    emailFeedBackArea.style.display="none"
    
    if(emailVal.length > 0){
        fetch("/auth/email_validation",{
            body:JSON.stringify({email: emailVal}),
            method:"POST"
        })
        .then((res) =>res.json())
        .then((data) =>{
            console.log("data",data)
            emailSuccessOutput.style.display="none"
            if(data.email_error){
                submitBtn.disabled=true;
                emailField.classList.add('is-invalid')
                emailFeedBackArea.style.display="block"
                emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`


            }else{
                submitBtn.removeAttribute('disabled')
            }
        })
    }

})


usernameField.addEventListener("keyup" , (e) => {

    const usernameVal = e.target.value;
    usernameField.classList.remove('is-invalid')
    feedBackArea.style.display="none"
    usernameSuccessOutput.textContent = `Checking ${usernameVal}`
    
    if(usernameVal.length > 0){
        fetch("/auth/username_validation",{
            body:JSON.stringify({username: usernameVal}),
            method:"POST"
        })
        .then((res) =>res.json())
        .then((data) =>{
            
            usernameSuccessOutput.style.display="none"
            if(data.username_error){
                submitBtn.disabled=true;
                usernameField.classList.add('is-invalid')
                feedBackArea.style.display="block"
                feedBackArea.innerHTML=`<p>${data.username_error}</p>`


            }else{
                submitBtn.removeAttribute('disabled')
            }
        })
    }
    
})

firstnameField.addEventListener("keyup" , (e) => {

    const firstnameVal = e.target.value;
    console.log(firstnameField)
    firstnameField.classList.remove('is-invalid')
    feedBackArea.style.display="none"
    firstnameSuccessOutput.textContent = `Checking ${firstnameVal}`
    
    if(firstnameVal.length > 0){
        fetch("/auth/firstname_validation",{
            body:JSON.stringify({first_name: firstnameVal}),
            method:"POST"
        })
        .then((res) =>res.json())
        .then((data) =>{
            console.log("data",data)
            firstnameSuccessOutput.style.display="none"
            if(data.firstname_error){
                submitBtn.disabled=true;
                firstnameField.classList.add('is-invalid')
                feedBackArea.style.display="block"
                feedBackArea.innerHTML=`<p>${data.firstname_error}</p>`


            }else{
                submitBtn.removeAttribute('disabled')
            }
        })
    }
    
})


lastnameField.addEventListener("keyup" , (e) => {

    const lastnameFieldVal = e.target.value;
    
    lastnameField.classList.remove('is-invalid')
    feedBackArea.style.display="none"
    lastnameSuccessOutput.textContent = `Checking ${lastnameFieldVal}`
    
    if(lastnameFieldVal.length > 0){
        fetch("/auth/lastname_validation",{
            body:JSON.stringify({last_name: lastnameFieldVal}),
            method:"POST"
        })
        .then((res) =>res.json())
        .then((data) =>{
            console.log("data",data)
            lastnameSuccessOutput.style.display="none"
            if(data.firstname_error){
                submitBtn.disabled=true;
                lastnameField.classList.add('is-invalid')
                feedBackArea.style.display="block"
                feedBackArea.innerHTML=`<p>${data.firstname_error}</p>`


            }else{
                submitBtn.removeAttribute('disabled')
            }
        })
    }
    
})