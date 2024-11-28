const { from } = require('rxjs');
const { filter, map, reduce } = require('rxjs/operators');

const people = [
    { name: 'Jan', age: 30, country: 'Poland' },
    { name: 'Anna', age: 25, country: 'Poland' },
    { name: 'John', age: 40, country: 'USA' },
    { name: 'Kasia', age: 35, country: 'Poland' },
    { name: 'Paweł', age: 28, country: 'Poland' },
    { name: 'Lisa', age: 32, country: 'USA' }
];

from(people)
  .pipe(
    filter(person => person.country === 'Poland'),
    map(person => person.age),
    reduce((acc, age) => acc + age, 0)
  )
  .subscribe({
    next: totalAge => {
      const count = people.filter(person => person.country === 'Poland').length;
      const averageAge = totalAge / count;
      console.log(`Average age of people living in Poland: ${averageAge}`);
    },
    error: err => console.error('Error:', err),
    complete: () => console.log('Calculation complete.')
  });
  