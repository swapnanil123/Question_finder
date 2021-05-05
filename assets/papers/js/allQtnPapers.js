
function fillModal(id) {
    console.log(id)
    console.log('HI')

    // qtnPaper = $('#qtnPaper_name_id_'+ id).text()
    subject = $('#subject_name_id_' + id).text()
    paper = $('#paper_name_id_' + id).text()
    course = $('#course_name_id_' + id).text()
    year = $('#year_id_' + id).text()

    console.log(subject, paper, course, year)

    $('#qtn_ID').val(id)
    $('#edit_subjectName').val(subject)
    $('#edit_paperName').val(paper)
    $('#edit_course').val(course)
    $('#edit_year').val(year)

}


function getName(){
    console.log('GET')
    file = $('#qtnPaperName')[0].files[0]
    
    console.log(file.name)

    $('#selector').text(file.name)
}