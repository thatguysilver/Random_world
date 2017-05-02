# A random fantasy world generator!
The goal of this project is to create a completely randomly-generated fantasy world and use the power of LaTeX to make a sort of miniature encyclopedia. The pages will be:

1. **Title page**: Self-explanatory.
2. **Introduction**: A breakdown of the demographics and geographic/geologic/climatological characteristics of the world.
3. **Magic system**: How the magic system in our world works. This one's turning out to be a bit of a thinker.
4. **Menagerie**: Randomly-generated critters and their characteristics.

To-do: 
1. Add automatic $pdflatex and rm \<auxiliary files> to the parts of the Generators class that make the pages
2. Add about 10x more randomly-generated characteristics to each page
3. Add a tremendous amount of syllables, consonants, and vowels to the word_generator
4. Add range arguments to the word_generator so people don't have five-syllable names and shit
5. Remove bloat from main.py

Future:
1. Consider making it a feature of a website, rather than a pdf-creator thing
2. Consider adding some basic visuals; for example, add some turtle-drawing for creatures with radial symmetry.
