document.getElementById('khmnk-gmail').addEventListener('click', function() {
    var emailAddress = 'khomenko.kiril1621@vu.cdu.edu.ua';
    navigator.clipboard.writeText(emailAddress);
    var hint = document.getElementById('hint');
    hint.style.display = 'block';

    setTimeout(function() {
        hint.style.display = 'none';
    }, 3000);
});

document.getElementById('dvdnk-gmail').addEventListener('click', function() {
    var emailAddress = 'davydenko.kirill1621@vu.cdu.edu.ua';
    navigator.clipboard.writeText(emailAddress);
    var hint = document.getElementById('hint');
    hint.style.display = 'block';

    setTimeout(function() {
        hint.style.display = 'none';
    }, 3000);
});
