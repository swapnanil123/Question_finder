
console.log('All Subjects are Shown properly');



function removeSubject(id) {
    console.log('Button clicked')

    console.log(id)

    $.ajax({

        url: '/deleteSubject/' + id,
        dataType: 'json',
        success: function (data) {
            console.log(data.status)
            $('#subject_id_' + id).remove()

            // $('#alert').text('Subject Deleted Successfully')
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



function editSubject(id) {
    console.log(id)

    tableSubjectName = $('#subject_name_id_' + id).text()
    tableStreamName = $('#stream_name_id_' + id).text()

    console.log(tableSubjectName, tableStreamName)

    $('#subjectID').val(id)
    $('#subject_name').val(tableSubjectName)
    $('#streamName').val(tableStreamName)
}

$('#editForm').on('submit', function (e) {
    e.preventDefault()

    id = $('#subjectID').val()
    subjectName = $('#subject_name').val()
    streamName = $('#streamName').val()
    csrf = $('input[name=csrfmiddlewaretoken]').val()

    console.log(id, subjectName, streamName)

    // text-transformation area

    lenOFSubjectName = subjectName.length

    var subjectFirstLetter = subjectName.substr(0, 1).toUpperCase()
    var excludingFirstSub = subjectName.substr(1, lenOFSubjectName).toLowerCase()
    var subjectCase = subjectFirstLetter.concat(excludingFirstSub)

    lenOfStreamName = subjectName.length

    var streamFirstLetter = streamName.substr(0, 1).toUpperCase()
    var excludeingFirstStre = streamName.substr(1, lenOfStreamName).toLowerCase()
    var streamCase = streamFirstLetter.concat(excludeingFirstStre)

    console.log(subjectCase, streamCase)

    // end

    $.ajax({

        url: '/editSubject',
        method: 'POST',
        data: {
            'id': id,
            'subjectName': subjectName,
            'streamName': streamName,
            'csrfmiddlewaretoken': csrf,
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.status)

            $('#subject_name_id_' + id).text(subjectCase)
            $('#stream_name_id_' + id).text(streamCase)

            $("#editForm").trigger("reset");

            $('#editSubjectModal').modal('hide');

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


// add part

console.log('hi, i am here')

$('#createSubjectForm').on('submit', function (e) {
    e.preventDefault()
    row = ''

    console.log('Form Submitted')

    subjectName = $('#subjectName').val()
    streamName = $('#stream').val()
    csrf = $('input[name=csrfmiddlewaretoken]').val()

    // text-transformation area

    lenOFSubjectName = subjectName.length

    var subjectFirstLetter = subjectName.substr(0, 1).toUpperCase()
    var excludingFirstSub = subjectName.substr(1, lenOFSubjectName).toLowerCase()
    var subjectCase = subjectFirstLetter.concat(excludingFirstSub)

    lenOfStreamName = streamName.length

    var streamFirstLetter = streamName.substr(0, 1).toUpperCase()
    var excludeingFirstStre = streamName.substr(1, lenOfStreamName).toLowerCase()
    var streamCase = streamFirstLetter.concat(excludeingFirstStre)

    console.log(subjectCase, streamCase)

    // end

    $.ajax({

        url: '/addSubject',
        method: 'POST',
        data: {
            'subjectName': subjectName,
            'streamName': streamName,
            'csrfmiddlewaretoken': csrf,
        },
        dataType: 'json',
        success: function (data) {

            if (data.status == 'success') {
                id = data.id

                row = "<tr id='subject_id_" + id + "'> <td id='subject_name_id_" + id + "'>" +
                    subjectCase + "</td><td id='stream_name_id_" + id + "'>" + streamCase +
                    "</td><td data-target='#editSubjectModal' data-toggle='modal' onclick='editSubject(" + id + ")'> <i class='fa fa-edit fa-lg event_icon'></i> </td> <td onclick = 'removeSubject(" +
                    id + ")'> <i class='fa fa-trash fa-lg event_icon'></i> </td></tr>"

                $('#subjectTableBody').append(row)

                $("#createSubjectForm").trigger("reset");

                $('#addSubjectModal').modal('hide');


            }
        },
        error: function (e) {
            console.log(e)
        }
    })
})
