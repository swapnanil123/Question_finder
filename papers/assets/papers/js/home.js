
console.log('Works perfectly')

function getPaperName() {
    console.log('Hi, I am Here')

    var selectedSubject = $('#subject').val()
    var sem = $('#semester').val()

    console.log(selectedSubject, sem)

    $.ajax({
        url: '/paperName/' + selectedSubject + '/' + sem,
        data: {},
        dataType: 'json',
        success: function (data) {
            console.log(data.status)
            // console.log(data.result)

            var paper = document.getElementById('paper')
            paper.innerHTML = ''
            if (data.status == 'success') {
                for (let i = 0; i < data.result.length; i++) {
                    const element = data.result[i];
                    var option = document.createElement('option')
                    option.setAttribute('value', element.paperName)
                    option.innerText = element.paperName
                    paper.appendChild(option);
                }
            } else if (data.status == 'failed') {
                console.log(data.msg)
                const element = data.msg;
                var option = document.createElement('option')
                option.setAttribute('value', element)
                option.innerText = element
                paper.appendChild(option);
            } else {
                const element = 'Select Paper Here';
                var option = document.createElement('option')
                option.setAttribute('value', element)
                option.innerText = element
                paper.appendChild(option);
            }
        },
        error: function (err) {
            console.log(err)
        }
    })
}



$('#qtnFileForm').on('submit', function (e) {


    // $("#qtnFileForm").trigger("reset");

    paperName = $('#paper').val()

    // console.log(subjectName, paperName);

    if (paperName != 'No Papers Found') {
        console.log('Paper Found')

    } else {
        console.log('Paper Not found')
        e.preventDefault()
        alert('Please Select Paper')
    }
})


$(document).ready(function () {
    console.log("ready!");

    setInterval(() => {
        $('#msg').fadeOut()
    }, 8000);
});
