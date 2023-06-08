# Why


> Aoccdrnig to rscheearch at Cmabrigde uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are, the olny iprmoatnt tihng is taht the frist and lsat ltteer be at the rghit pclae

This is a simple script that will take a string and scramble the letters in each
word, but keep the first and last letter in place. This is to investigate the above
claim, since I could in fact read it, though not quite as fast. We take a random
line from a file and scramble it, then print it out along with the original line.

How hard was it to read? I found short words often are in the right order and
give scaffolding to the longer ones. Sentences full of long words are much
harder, but usually doable. Sometimes the scrambling is not too far off and the
scrambled words have similar shape to the originals, which makes it much easier
for me.

## Usage

`python3 first_and_last_word` (implicitly runs `first_and_last_word/__main__.py`)

Or use your file:

`python3 first_and_last_word --file <file>`
