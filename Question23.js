{
    var car = 'subaru';
    console.log("Is car == 'subaru'? I predict True.");
    console.log(car == 'subaru');
    console.log("Is car == 'toyota'? I predict False.");
    console.log(car == 'toyota');
}
{
    var age = 25;
    console.log("Is age > 18? I predict True.");
    console.log(age > 18);
    console.log("Is age < 21? I predict False.");
    console.log(age < 21);
}
{
    var isRaining = true;
    console.log("Is isRaining? I predict True.");
    console.log(isRaining);
    console.log("Is isRaining? I predict False.");
    console.log(!isRaining);
}
{
    var fruits = ['apple', 'orange', 'banana'];
    console.log("Does 'apple' exist in fruits? I predict True.");
    console.log(fruits.indexOf('apple') != -1);
    console.log("Does 'grape' exist in fruits? I predict False.");
    console.log(fruits.indexOf('grape') == 1);
}
{
    var person = { name: 'John', age: 30 };
    console.log("Is person's age less than 40? I predict True.");
    console.log(person.age < 40);
    console.log("Is person's age greater than or equal to 35? I predict False.");
    console.log(person.age >= 35);
}
