console.log("All Right")

function removePaper(id) {
    console.log(id)

    $.ajax({

        url: '/deletePaper/' + id,
        dataType: 'json',
        success: function (data) {
            console.log(data.status)

            $('#paper_id_' + id).remove()

            // $('#alert').text('Paper Deleted Successfully')
            // $('#alert').addClass("alert alert-danger");
            // $('#alert').show()
            // setInterval(() => {
            //     $('#alert').fadeOut()
            // }, 5000);
        },
        error: function (e) {
            console.log(e)
        }
    })
}


function editPaper(id) {
    console.log(id)

    tablePaperName = $('#paperName_id_' + id).text()
    tableSubjectmName = $('#subjectName_id_' + id).text()
    tableSemesterName = $('#semesterName_id_' + id).text()

    console.log(tablePaperName, tableSubjectmName, tableSemesterName)

    $('#paperID').val(id)
    $('#paper_name').val(tablePaperName)
    $('#subject_name').val(tableSubjectmName)
    $('#semester_name').val(tableSemesterName)

}


$('#editForm').on('submit', function (e) {
    e.preventDefault()

    id = $('#paperID').val()
    subjectName = $('#subject_name').val()
    paperName = $('#paper_name').val()
    semesterName = $('#semester_name').val()
    csrf = $('input[name=csrfmiddlewaretoken]').val()

    console.log(id, subjectName, paperName, semesterName)

    // text-transformation area

    lenOFSubjectName = subjectName.length

    var subjectFirstLetter = subjectName.substr(0, 1).toUpperCase()
    var excludingFirstSub = subjectName.substr(1, lenOFSubjectName).toLowerCase()
    var subjectCase = subjectFirstLetter.concat(excludingFirstSub)

    lenOfStreamName = paperName.length

    var paperFirstLetter = paperName.substr(0, 1).toUpperCase()
    var excludeingFirstStre = paperName.substr(1, lenOfStreamName).toLowerCase()
    var paperCase = paperFirstLetter.concat(excludeingFirstStre)

    lenOfSemesterName = semesterName.length

    var semFirstLetter = semesterName.substr(0, 1).toUpperCase()
    var excludeingFirstStre = semesterName.substr(1, lenOfStreamName).toLowerCase()
    var semCase = semFirstLetter.concat(excludeingFirstStre)

    console.log(subjectCase, paperCase, semCase)

    // end

    $.ajax({

        url: '/editpaper',
        method: 'POST',
        data: {
            'id': id,
            'subjectName': subjectName,
            'paperName': paperName,
            'semester': semesterName,
            'csrfmiddlewaretoken': csrf,
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.status)

            $('#subjectName_id_' + id).text(subjectCase)
            $('#paperName_id_' + id).text(paperCase)
            $('#semesterName_id_' + id).text(semCase)

            $("#editForm").trigger("reset");

            $('#editPaperModal').modal('hide');

            // $('#alert').text('Subject Edit Successfully')
            // $('#alert').addClass("alert alert-success");
            // $('#alert').show()
            // setInterval(() => {
            //     $('#alert').fadeOut()
            // }, 5000);

        },
        error: function (e) {
            console.log(e)
        }
    })

})


// asdfljasdjflkasdjf



console.log('hi')

$('#addPaperModal').on('submit', function (e) {
    e.preventDefault()
    row = ''

    console.log('Form Submitted')

    paperName = $('#paperName').val()
    subjectName = $('#subjectName').val()
    semesterName = $('#semesterName').val()
    csrf = $('input[name=csrfmiddlewaretoken]').val()

    console.log(paperName, subjectName)

    // text-transformation area

    lenOFSubjectName = subjectName.length

    var subjectFirstLetter = subjectName.substr(0, 1).toUpperCase()
    var excludingFirstSub = subjectName.substr(1, lenOFSubjectName).toLowerCase()
    var subjectCase = subjectFirstLetter.concat(excludingFirstSub)

    lenOfStreamName = paperName.length

    var paperFirstLetter = paperName.substr(0, 1).toUpperCase()
    var excludeingFirstStre = paperName.substr(1, lenOfStreamName).toLowerCase()
    var paperCase = paperFirstLetter.concat(excludeingFirstStre)

    lenOfSemesterName = semesterName.length

    var semFirstLetter = semesterName.substr(0, 1).toUpperCase()
    var excludeingFirstStre = semesterName.substr(1, lenOfStreamName).toLowerCase()
    var semCase = semFirstLetter.concat(excludeingFirstStre)


    console.log(subjectCase, paperCase, semCase)

    // end

    $.ajax({

        url: '/addPaper',
        method: 'POST',
        data: {
            'subjectName': subjectName,
            'paperName': paperName,
            'semName': semesterName,
            'csrfmiddlewaretoken': csrf,
        },
        dataType: 'json',
        success: function (data) {

            if (data.status == 'success') {
                id = data.id

                console.log(id)

                row = "<tr id='paper_id_" + id + "'> <td id='paperName_id_" + id + "'>" +
                    paperCase + "</td><td id='subjectName_id_" + id + "'>" + subjectCase +
                    "</td><td id='semesterName_id_" + id + "'>" + semCase +"</td><td data-target='#editPaperModal' data-toggle='modal' onclick='editPaper(" + id + ")'> <i class='fa fa-edit fa-lg event_icon'></i> </td> <td onclick = 'removePaper(" +
                    id + ")'> <i class='fa fa-trash fa-lg event_icon'></i> </td></tr>"

                $('#papertableBody').append(row)

                $("#createPaperForm").trigger("reset");

                $('#addPaperModal').modal('hide');

                // $('#alert').text('Subject Edit Successfully')
                // $('#alert').addClass("alert alert-success");
                // $('#alert').show()
                // setInterval(() => {
                //     $('#alert').fadeOut()
                // }, 5000);
            }

        },
        error: function (e) {
            console.log(e)
        }
    })
})