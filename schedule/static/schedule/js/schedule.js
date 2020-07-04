$(document).ready(function () {
    $("#type").change(function () {

        var arr = $(this).val();

        if(arr == "teachers_schedule"){
        	$("#changing-text").text("Вчитель");
        	$("#classes").hide();
            $("#teachers").show();
        }
        else if(arr == "students_schedule"){
        	$("#changing-text").text("Клас");
        	$("#classes").show();
            $("#teachers").hide();
        }
    });
});