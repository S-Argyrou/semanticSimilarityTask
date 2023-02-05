# Importing spacy
import spacy  

# Specify the model we want to use.
nlp = spacy.load('en_core_web_md')

def watch_next(des):
      """
      Takes in a description of a just-watched movie and
      return which movie a person should watch next,      

      Keyword arguments:
      des (str): the description of the movie just watched.

      Returns:
      title of most similar movie.
      """     
      # Open the file in read mode.
      with open('movies.txt') as f:
            # Create an empty list to append the plots.  
            plots = []

            # Read file content and store it in a variable.
            content = f.readlines()

            # Append everyline in 'plot' list.
            for line in content:
                  plots.append(line)
                  

      # Assign the content of description to a variable.
      movie_to_compare = des

      # Assign to the description nlp module.
      des = nlp(des)

      # Create an empty dictionary to store titles as key and plots as values.
      titles = {}

      # Loop through every movie in the list.
      for plot in plots:

            # Split each line at ' :'
            data = plot.split(' :')

            # Assign the first field to the variable 'title.'
            title = data[0]

            # Assign the second field to the variable 'description'.
            description = data[1]

            # Compare each description with the just-watched movie description.
            similarity = nlp(description).similarity(des)            

            # Set titles as key and plots as dictionary values.
            titles[title] = similarity    

            # Look for the value in dictionary with the highest value.
            max_value = max(titles, key=titles.get)
            
      # Return highest value.
      return max_value



# Store movie description in a variable.
descrip = """Will he save their world or destroy it?
      When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and
      launch him into space to a planet where the Hulk can live in peace.
      Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Print formatted message. 
print(f"You should watch next: {watch_next(descrip)}")

    
    
