const findSeashellsIndices = (target, array) => {
    const indexMap = new Map();
    const indexesArray = [];
    
    for (let i = 0; i < array.length; i++) {
        if (indexMap.has(target - array[i])) {
            indexesArray.push([indexMap.get(target - array[i]), i]);
        }
        indexMap.set(array[i], i);
    }
    return indexesArray;
}
console.log( findSeashellsIndices(30, [5, 10, 15, 21, 25]));
