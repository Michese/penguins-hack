export default [...(function* () {
    for (let index = 1; index <= 10; index++) {
        yield `f${index}`;
    }
})()];