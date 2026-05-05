$(document).ready(function () {

    $("#id_wilaya").change(function () {

        var wilayaId = $(this).val();

        $.ajax({
            url: "/ajax/load-communes/",
            data: {
                'wilaya': wilayaId
            },
            success: function (data) {

                $("#id_commune").html("");

                data.forEach(function (item) {
                    $("#id_commune").append(
                        `<option value="${item.id}">${item.name_fr}</option>`
                    );
                });

            }
        });

    });

});