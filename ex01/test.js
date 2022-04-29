list1 = [1, 2, 3]

// console.log(list1)

// 스프레드 : for문을 돌면서 가지고 있는 데이터를 하나씩 꺼낸다
list1 = [...list1, 4]

// console.log(list1)

// let user = {
//     id: 1,
//     username: "cos"
// }

// user2 = {...user }
// console.log(user2)

// let users = [key{
//         id: 1,
//         username: "cos"
//     },
//     {
//         id: 2,
//         username: "ssar"
//     }
// ]

// let updateUsers = [...users, { id: 2, username: "hello" }]

// console.log(updateUsers)

let user = {
    id: 1,
    username: "cos"
}
console.log(user)

user = {...user, id: 2 }
console.log(user)