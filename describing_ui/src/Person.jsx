const person = {
    name: 'Gregorio Y. Zara',
    theme: {
        backgroundColor: 'black',
        color: 'pink'
    }
};

export default function Person() {
    return (
        <>
            <div style={person.theme}>
                <h1>{person.name}'s Todos</h1>
                <img src="https://i.imgur.com/7vQD0fPs.jpg" alt="Gregorio Y. Zara" className="avatar" />
            </div>
            <ul>
                <li>improve videophone</li>
                <li>prepare aeronautics lectures</li>
                <li>work on the alcohol-fueled engine</li>
            </ul>
        </>
    );
}