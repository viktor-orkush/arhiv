function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    add_total_form = $('#id_form-TOTAL_FORMS').val();
    $('#id_form-TOTAL_FORMS').val(parseInt(add_total_form)+1);
    newElement.find('input').each(function () {
        var tID = $(this).attr("name").split('-');
        var re = parseInt(tID[1]);
        var newID = $(this).attr('id').replace(re, (re + 1));
        var newName = $(this).attr('name').replace(re, (re + 1));
        $(this).attr({'name': newName, 'id': newID}).val('');
    });
//           newElement.find('label').each(function () {
//               var newFor = $(this).attr('for').replace('-' + (total - 1) + '-', '-' + total + '-');
//                $(this).attr('for', newFor);
//            );
    $(selector).after(newElement);

    newElement.find('#add_more')
        .attr('id', 'remove')
        .removeClass('btn-success')
        .addClass('btn-danger')
        .html('-');
};

function deleteForm(prefix, btn) {
    total_form = $('#id_form-TOTAL_FORMS').val();
    $('#id_form-TOTAL_FORMS').val(parseInt(total_form)-1);
    $(btn).parent().parent().parent().remove();
    return false;
}