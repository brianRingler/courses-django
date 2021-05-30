// GOOD HELP https://stackoverflow.com/questions/62416617/add-csrf-in-fetch-js-for-django

// MAYBE HELP?? https://stackoverflow.com/questions/43606056/proper-django-csrf-validation-using-fetch-post-request

// FORM DATA https://javascript.info/formdata

// https://www.youtube.com/watch?v=cuEtnrL9-H0

// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
// Post data response for add_courses validation

// get the csrf token for passing data POST
// getCookie is function from Django docs

const courseName = document.querySelector('#course-name');
const courseDesc = document.querySelector('#course-desc');
if(courseName === "" || courseName === null){
    console.log('courseName is empty/null');
}else{
    console.log(`Course Name is: ${courseName.value}`);
}
if(courseDesc === "" || courseDesc === null){
    console.log('courseName is empty/null');
}else{
    console.log(`Course Name is: ${courseName.value}`);
    console.log(typeof courseName.value);
}

console.log(`${courseName.value} ${courseDesc.value}`);

// create dummy data for testing
formData = {
    'course-name-nm' : 'd',
    'course-desc-nm' : 'd',
}

let csrfToken = getCookie("csrftoken");
addCourseID.onsubmit = async (e) => {
    e.preventDefault();
    try {
        let response = await fetch("/", {
            method: 'POST',
            credentials: 'same-origin', // required
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: formData
    });
            // let data = await response.json();
            let data = await response.text();
            console.log(data);

    } catch (error) {
           console.log('****ERROR MESSAGE****'); 
           console.log(error);
    }   
}



// get the csrf token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}