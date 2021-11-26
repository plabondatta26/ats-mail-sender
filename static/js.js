var endpoint1 = '/get/emails/'
var dataset = []
$(document).ready(function() {
    dataset = []
    $.ajax({
        method: "GET",
        url: endpoint1,
        success: function(data) {
            $('#email_table').empty()
            dataset.push(data)
            $.each(data, function(key, value) {
                $('#email_table').append('<tr><td> <input type="checkbox" id="' + value.id + '" style="margin-right: 3px;" onclick="checked_box(' + value.id + ')">' + value.email + '</td></tr>');
            })
        }
    });
})

function refresh_email() {
    dataset = []
    $.ajax({
        method: "GET",
        url: endpoint1,
        success: function(data) {
            $('#email_table').empty()
            dataset.push(data)
            $.each(data, function(key, value) {
                $('#email_table').append('<tr><td> <input type="checkbox" id="' + value.id + '" style="margin-right: 3px;" onclick="checked_box(' + value.id + ')">' + value.email + '</td></tr>');
            })
        }
    });
}

function checked_box(id) {

    chkbox = document.getElementById(id)
    for (i = 0; i < dataset[0].length; i++) {

        if (dataset[0][i].id === id) {
            if (chkbox.checked) {
                $('#recipient').append(dataset[0][i].email + ',')
            } else {
                var textarea = document.getElementById("recipient").value;
                const myArray = textarea.split(',');
                $('#recipient').empty()
                for (var j = 0; j < myArray.length; j++) {
                    console.log(myArray[j]);
                    if (myArray[j] === dataset[0][i].email) {
                        myArray.splice(j)
                    } else {
                        $('#recipient').append(myArray[j] + ',')
                    }
                }

            }

        }
    }

}