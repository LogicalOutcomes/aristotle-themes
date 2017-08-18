// Checkbox all of paginated list
$(document).ready(function() {
    $(document).on('change', '#all_in_queryset', function(e){
        var $allCheckbox = $(this),
            $table = $allCheckbox.closest('table'),
            $checkboxes = $table.find('input[name=items]');

        if( $allCheckbox.is(':checked') ){
            $checkboxes.prop('checked', true);
        } else {
            $checkboxes.prop('checked', false);
        }
    });
});