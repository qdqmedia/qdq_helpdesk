$(document).ready(function () {

    if ($('.messages').length > 0) {
            $('.messages').fadeOut(3000);
    }

    $('.btn-del-attached-file').click(function() {
        if (!confirm("¿Seguro que desea borrar este fichero?")) {
            return false;
        }
    });
});

