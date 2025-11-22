import { recipes } from "./recipe_data";

// export default function RecipeList() {
//     return (
//         <div>
//             <h1>Recipes</h1>
//             {recipes.map(recipe =>
//                 <div key={recipe.id}>
//                     <h2>{recipe.name}</h2>
//                     <ul>
//                         {recipe.ingredients.map(ingredient =>
//                             <li key={ingredient}>
//                                 {ingredient}
//                             </li>
//                         )}
//                     </ul>
//                 </div>
//             )}
//         </div>
//     );
// }

function Recipe({ id, name, ingredients }) {
    return (
        <div>
            <h2>name</h2>
            <ul>
                {ingredients.map(ingredient =>
                    <li key={ingredient}>
                        {ingredient}
                    </li>
                )}
            </ul>
        </div>
    )
}
export default function RecipeList() {
    return (
        <div>
            <h1>Recipes</h1>
            {
                recipes.map(recipe =>
                    <Recipe {...recipe} key={recipe.id} />
                )
            }
        </div>
    )
}