document.addEventListener('DOMContentLoaded', function () {
  const imageBlock = document.querySelector('.image-block');
  const textBlock = document.querySelector('.slide-text');
  const prevButton = document.querySelector('.prev-button');
  const nextButton = document.querySelector('.next-button');

  let currentIndex = 0;
  let persons = [];

  fetch('/get-slider-data')
    .then(response => response.json())
    .then(data => {
      persons = data;
      updateSlide();
    });

  function updateSlide() {
    if (persons.length === 0) {
      imageBlock.style.backgroundImage = 'none';
      prevButton.disabled = true;
      nextButton.disabled = true;
      return;
    }
    const person = persons[currentIndex];
    imageBlock.style.backgroundImage = `url('data:image/jpeg;base64,${person.image}')`;
    textBlock.innerHTML = `
        Прізвище: ${person.surname} <br><br>
        Ім'я: ${person.name} <br><br>
        По батькові: ${person.middle_name} <br><br>
        Вік: ${person.age} <br><br>
        Рід занять: ${person.occupation} <br><br>
        Спеціалізація: ${person.specialization} <br>`;
  }

  prevButton.addEventListener('click', function () {
    currentIndex = (currentIndex - 1 + persons.length) % persons.length;
    updateSlide();
  });

  nextButton.addEventListener('click', function () {
    currentIndex = (currentIndex + 1) % persons.length;
    updateSlide();
  });

});
