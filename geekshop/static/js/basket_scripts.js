window.onload = function () {
    console.log('DOM Loaded');
    $('.arts_block').on('change', 'input[type=number]', function (event) {
        console.log(event.target);
        $.ajax({
            url: '/basket/change/' + event.target.name + '/quantity/' + event.target.value + '/',
            success: function (data) {
                console.log(data)
                $('.arts_block').html(data.result);
            }
        });
    })
};
