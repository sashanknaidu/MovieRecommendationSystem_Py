import pandas as pd

class TeluguMovieRecommender:
    def __init__(self):
        # Expanded Telugu movie database with more movies from popular actors
        self.movies_data = {
            'title': [
                # Previous movies
                'Baahubali: The Beginning &The Conclusion', 'RRR', 'Pushpa: The Rise', 
                'Arya', 'Okkadu', 'Chatrapathi', 'Jersey',
                'Eega', 'Magadheera', 'Pokiri',
                'Sye Raa Narasimha Reddy', 'Sarileru Neekevvaru', 'Ala Vaikunthapurramuloo',
                
                # Prabhas Movies
                'Baahubali 2: The Conclusion', 'Saaho', 'Mirchi',
                'Mr. Perfect', 'Darling', 'Billa',
                'Varsham', 'Rebel', 'Ek Niranjan',
                
                # Mahesh Babu Movies
                'Srimanthudu', 'Bharat Ane Nenu', 'Spyder',
                'Businessman', '1: Nenokkadine', 'Khaleja',
                'Athadu', 'Guntur Kaaram', 'Aagadu',
                
                # Allu Arjun Movies
                'Pushpa 2: The Rule', 'Bunny', 'Race Gurram',
                'S/O Satyamurthy', 'Naa Peru Surya', 'Vedam',
                'Happy', 'Desamuduru', 'Parugu',
                
                # NTR Jr Movies
                'Devara', 'Aravinda Sametha', 'Jai Lava Kusa',
                'Nannaku Prematho', 'Temper', 'Baadshah',
                'Yamadonga', 'Adhurs', 'Simhadri',
                
                # Ram Charan Movies
                'Orange', 'Dhruva', 'Rangasthalam',
                'Yevadu', 'Naayak', 'Zanjeer',
                'Chirutha', 'Bruce Lee', 'Vinaya Vidheya Rama',
                
                # Pawan Kalyan Movies
                'Vakeel Saab', 'Agnyaathavaasi', 'Sardaar Gabbar Singh',
                'Attarintiki Daredi', 'Cameraman Gangatho Rambabu', 'Jalsa',
                'Tholiprema', 'Johnny', 'Balu',
                
                # Ravi Teja Movies
                'Krack', 'Disco Raja', 'Bengal Tiger',
                'Kick', 'Don Seenu', 'Krishna',
                'Vikramarkudu', 'Itlu Sravani Subramanyam', 'Venky',
                
                # Nani Movies
                'Gang Leader', 'V', 'MCA',
                'Krishnarjuna Yuddham', 'Gentleman', 'Eega',
                'Ante Sundaraniki', 'Shyam Singha Roy', 'Tuck Jagadish',
                
                # Vijay Deverakonda Movies
                'Liger', 'Dear Comrade', 'Geetha Govindam',
                'Taxiwaala', 'Pelli Choopulu', 'World Famous Lover',
                'NOTA', 'Kushi', 'Family Star'
            ],
            'genre': [
                # Previous genres
                'Action,Drama,Fantasy', 'Action,Drama,Historical', 'Action,Crime,Drama',
                'Romance,Comedy', 'Action,Romance', 'Action,Drama',
                'Drama,Sport', 'Fantasy,Action', 'Action,Romance,Fantasy',
                'Action,Crime', 'Action,Historical,Drama', 'Action,Comedy',
                'Action,Comedy,Drama',
                
                # Additional movies genres
                'Action,Drama,Fantasy', 'Action,Thriller', 'Action,Romance',
                'Romance,Drama', 'Romance,Comedy', 'Action,Thriller',
                'Romance,Drama', 'Action,Drama', 'Action,Romance',
                
                'Drama,Social', 'Political,Drama', 'Action,Thriller',
                'Action,Crime', 'Psychological,Thriller', 'Comedy,Drama',
                'Action,Thriller', 'Action,Drama', 'Action,Comedy',
                
                'Action,Drama', 'Romance,Comedy', 'Action,Comedy',
                'Family,Drama', 'Action,Patriotic', 'Drama,Social',
                'Romance,Comedy', 'Action,Romance', 'Romance,Action',
                
                'Action,Drama', 'Action,Family', 'Action,Drama',
                'Action,Thriller', 'Action,Drama', 'Action,Comedy',
                'Fantasy,Action', 'Comedy,Action', 'Action,Drama',
                
                'Romance,Drama', 'Action,Thriller', 'Period,Drama',
                'Action,Thriller', 'Action,Comedy', 'Action,Drama',
                'Action,Romance', 'Action,Drama', 'Action,Drama',
                
                'Courtroom,Drama', 'Action,Drama', 'Action,Romance',
                'Family,Comedy', 'Political,Drama', 'Action,Comedy',
                'Romance,Drama', 'Action,Romance', 'Romance,Drama',
                
                'Action,Comedy', 'Sci-fi,Action', 'Action,Comedy',
                'Action,Comedy', 'Comedy,Action', 'Romance,Action',
                'Action,Comedy', 'Romance,Drama', 'Comedy,Drama',
                
                'Comedy,Crime', 'Action,Thriller', 'Romance,Drama',
                'Romance,Action', 'Crime,Thriller', 'Fantasy,Action',
                'Romance,Comedy', 'Period,Romance', 'Family,Drama',
                
                'Sports,Action', 'Romance,Drama', 'Romance,Comedy',
                'Supernatural,Comedy', 'Romance,Comedy', 'Romance,Drama',
                'Political,Drama', 'Romance,Drama', 'Family,Drama'
            ],
            'sub_genre': [
                # Previous sub-genres (first 13 entries remain same)
                'Epic,War', 'Period,Friendship', 'Crime,Thriller',
                'Feel-good,Musical', 'Family,Social', 'Revenge,Family',
                'Family,Emotional', 'Revenge,Supernatural', 'Reincarnation,Period',
                'Crime,Thriller', 'Period,Patriotic', 'Military,Family',
                'Family,Musical',
                
                # Additional movies sub-genres
                'Epic,War', 'Heist,Technology', 'Family,Mass',
                'Love,Family', 'Comedy,Love', 'Gangster,Stylish',
                'Love,Musical', 'Mass,Action', 'Action,Romance',
                
                'Social,Message', 'Politics,Youth', 'Spy,Technology',
                'Mafia,Crime', 'Psychological,Mystery', 'Village,Fantasy',
                'Crime,Revenge', 'Mass,Entertainment', 'Mass,Comedy',
                
                'Forest,Crime', 'College,Fun', 'Entertainment,Comedy',
                'Family,Values', 'Army,Patriotic', 'Social,Message',
                'College,Romance', 'Mass,Love', 'Family,Romance',
                
                'Period,Action', 'Village,Family', 'Triple Role,Drama',
                'Revenge,Business', 'Police,Crime', 'Entertainment,Mass',
                'Mythology,Fantasy', 'Comedy,Double Role', 'Mass,Commercial',
                
                'Love,Musical', 'Police,Crime', 'Village,Period',
                'Identity,Thriller', 'Mass,Entertainment', 'Bilingual,Action',
                'Introduction,Action', 'Martial Arts,Family', 'Mass,Action',
                
                'Legal,Social', 'Business,Family', 'Police,Romance',
                'Family,Entertainment', 'Politics,Media', 'Dance,Entertainment',
                'Pure Love,Musical', 'Psychological,Action', 'Love,College',
                
                'Police,Mass', 'Sci-fi,Thriller', 'Comedy,Mass',
                'Entertainment,Fun', 'Mass,Comedy', 'Love,Action',
                'Police,Village', 'Love Story,Drama', 'Fun,Family',
                
                'Crime,Comedy', 'Vampire,Action', 'Middle Class,Romance',
                'Love,Fantasy', 'Crime,Love', 'Fantasy,Romance',
                'Brahmin,Comedy', 'Period,Supernatural', 'Village,Family',
                
                'Boxing,Drama', 'Student Politics,Love', 'College,Romance',
                'Ghost,Comedy', 'Small Business,Romance', 'Love,Emotional',
                'State Politics,Drama', 'Love,Family', 'Middle Class,Family'
            ],
            'actors': [
                # Previous actors (first 13 entries remain same)
                'Prabhas,Rana', 'NTR,Ram Charan', 'Allu Arjun,Rashmika',
                'Allu Arjun,Anuradha', 'Mahesh Babu,Bhumika', 'Prabhas,Shriya',
                'Nani,Shraddha', 'Sudeep,Samantha', 'Ram Charan,Kajal',
                'Mahesh Babu,Ileana', 'Chiranjeevi,Nayanthara', 'Mahesh Babu,Rashmika',
                'Allu Arjun,Pooja Hegde',
                
                # Additional movies actors
                'Prabhas,Anushka', 'Prabhas,Shraddha', 'Prabhas,Anushka',
                'Prabhas,Kajal', 'Prabhas,Deepika', 'Prabhas,Anushka',
                'Prabhas,Trisha', 'Prabhas,Tamannaah', 'Prabhas,Kangana',
                
                'Mahesh Babu,Shruti', 'Mahesh Babu,Kiara', 'Mahesh Babu,Rakul',
                'Mahesh Babu,Kajal', 'Mahesh Babu,Kriti', 'Mahesh Babu,Anushka',
                'Mahesh Babu,Trisha', 'Mahesh Babu,Meenakshi', 'Mahesh Babu,Tamannah',
                
                'Allu Arjun,Rashmika', 'Allu Arjun,Gowri', 'Allu Arjun,Shruti',
                'Allu Arjun,Samantha', 'Allu Arjun,Anu', 'Allu Arjun,Anushka',
                'Allu Arjun,Genelia', 'Allu Arjun,Hansika', 'Allu Arjun,Sheela',
                
                'NTR,Janhvi', 'NTR,Pooja', 'NTR,Nivetha',
                'NTR,Rakul', 'NTR,Kajal', 'NTR,Kajal',
                'NTR,Priyamani', 'NTR,Nayanthara', 'NTR,Bhumika',
                
                'Ram Charan,Genelia', 'Ram Charan,Rakul', 'Ram Charan,Samantha',
                'Ram Charan,Shruti', 'Ram Charan,Kajal', 'Ram Charan,Priyanka',
                'Ram Charan,Neha', 'Ram Charan,Rakul', 'Ram Charan,Kiara',
                
                'Pawan Kalyan,Shruti', 'Pawan Kalyan,Keerthy', 'Pawan Kalyan,Kajal',
                'Pawan Kalyan,Samantha', 'Pawan Kalyan,Tamannah', 'Pawan Kalyan,Ileana',
                'Pawan Kalyan,Keerthy', 'Pawan Kalyan,Renu', 'Pawan Kalyan,Shriya',
                
                'Ravi Teja,Shruti', 'Ravi Teja,Nabha', 'Ravi Teja,Tamannaah',
                'Ravi Teja,Ileana', 'Ravi Teja,Anjali', 'Ravi Teja,Trisha',
                'Ravi Teja,Anushka', 'Ravi Teja,Preeti', 'Ravi Teja,Nayanthara',
                
                'Nani,Priyanka', 'Nani,Sudheer', 'Nani,Sai Pallavi',
                'Nani,Anupama', 'Nani,Nivetha', 'Nani,Samantha',
                'Nani,Nazriya', 'Nani,Sai Pallavi', 'Nani,Ritu Varma',
                
                'Vijay,Ananya', 'Vijay,Rashmika', 'Vijay,Rashmika',
                'Vijay,Priyanka', 'Vijay,Ritu', 'Vijay,Raashi',
                'Vijay,Mehreen', 'Vijay,Samantha', 'Vijay,Mrunal'
            ]
        }
        self.df = pd.DataFrame(self.movies_data)
        self.prepare_data()

    def prepare_data(self):
        # Convert the comma-separated strings to lists
        self.df['genre_list'] = self.df['genre'].str.split(',')
        self.df['sub_genre_list'] = self.df['sub_genre'].str.split(',')
        self.df['actors_list'] = self.df['actors'].str.split(',')
        
        # Create sets of unique genres, sub-genres, and actors for validation
        self.available_genres = set()
        self.available_sub_genres = set()
        self.available_actors = set()
        
        for genres in self.df['genre_list']:
            self.available_genres.update(genres)
        for sub_genres in self.df['sub_genre_list']:
            self.available_sub_genres.update(sub_genres)
        for actors in self.df['actors_list']:
            self.available_actors.update(actors)

    def get_available_options(self):
        """Display available options for user selection"""
        print("\nAvailable Genres:", ', '.join(sorted(self.available_genres)))
        print("\nAvailable Sub-genres:", ', '.join(sorted(self.available_sub_genres)))
        print("\nAvailable Actors:", ', '.join(sorted(self.available_actors)))

    def calculate_similarity_score(self, row, preferences):
        """Calculate similarity score between a movie and user preferences"""
        score = 0
        
        # Check genre matches
        if preferences.get('genre'):
            genre_match = sum(1 for genre in row['genre_list'] 
                            if preferences['genre'].lower() in genre.lower())
            score += genre_match * 4
        
        # Check sub-genre matches
        if preferences.get('sub_genre'):
            subgenre_match = sum(1 for subgenre in row['sub_genre_list'] 
                               if preferences['sub_genre'].lower() in subgenre.lower())
            score += subgenre_match * 3
        
        # Check actor matches
        if preferences.get('actor'):
            actor_match = sum(1 for actor in row['actors_list'] 
                            if preferences['actor'].lower() in actor.lower())
            score += actor_match * 3
        
        return score

    def get_recommendations(self, preferences):
        """Get movie recommendations based on user preferences"""
        # Calculate similarity scores for all movies
        self.df['similarity_score'] = self.df.apply(
            lambda row: self.calculate_similarity_score(row, preferences), axis=1
        )
        
        # Sort movies by similarity score
        recommended_movies = (self.df[self.df['similarity_score'] > 0]
                            .sort_values('similarity_score', ascending=False)
                            .head(5))
        
        # Convert to list of dictionaries for output
        recommendations = []
        for _, movie in recommended_movies.iterrows():
            recommendations.append({
                'title': movie['title'],
                'genre': movie['genre'],
                'sub_genre': movie['sub_genre'],
                'actors': movie['actors'],
                'similarity_score': movie['similarity_score']
            })
        
        return recommendations

def get_user_input(recommender):
    """Get and validate user input"""
    recommender.get_available_options()
    
    print("\nPlease enter your preferences (press Enter to skip):")
    
    # Get genre input
    while True:
        genre = input("\nEnter preferred genre: ").strip()
        if not genre:  # Allow empty input
            genre = None
            break
        if any(genre.lower() in g.lower() for g in recommender.available_genres):
            break
        print("Invalid genre! Please choose from the available genres.")
    
    # Get sub-genre input
    while True:
        sub_genre = input("Enter preferred sub-genre: ").strip()
        if not sub_genre:  # Allow empty input
            sub_genre = None
            break
        if any(sub_genre.lower() in sg.lower() for sg in recommender.available_sub_genres):
            break
        print("Invalid sub-genre! Please choose from the available sub-genres.")
    
    # Get actor input
    while True:
        actor = input("Enter preferred actor: ").strip()
        if not actor:  # Allow empty input
            actor = None
            break
        if any(actor.lower() in a.lower() for a in recommender.available_actors):
            break
        print("Invalid actor! Please choose from the available actors.")
    
    return {
        'genre': genre,
        'sub_genre': sub_genre,
        'actor': actor
    }

def main():
    # Initialize the recommender
    recommender = TeluguMovieRecommender()
    
    while True:
        # Get user preferences through input
        preferences = get_user_input(recommender)
        
        # Check if at least one preference is provided
        if not any(preferences.values()):
            print("\nPlease provide at least one preference!")
            continue
        
        # Get recommendations
        recommendations = recommender.get_recommendations(preferences)
        
        # Print recommendations
        if recommendations:
            print("\nRecommended Movies based on your preferences:")
            print("============================================")
            for i, movie in enumerate(recommendations, 1):
                print(f"\n{i}. {movie['title']}")
                print(f"   Genre: {movie['genre']}")
                print(f"   Sub-genre: {movie['sub_genre']}")
                print(f"   Actors: {movie['actors']}")
                print(f"   Match Score: {movie['similarity_score']:.2f}")
        else:
            print("\nNo movies found matching your preferences.")
        
        # Ask if user wants to try again
        if input("\nWould you like to try another search? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()