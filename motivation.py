import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def create_venn_diagram(words):
    # Randomly select unique words for the circles and the center
    selected_words = random.sample(words, 4)  # 4 words (3 for circles + 1 for center)
    circle_words = selected_words[:3]          # First 3 for the circles
    center_word = selected_words[3]            # Last one for the center

    fig, ax = plt.subplots(figsize=(8, 8))

    # Define circles
    circle1 = patches.Circle((0.3, 0.5), 0.2, color='black', alpha=0.1)
    circle2 = patches.Circle((0.5, 0.5), 0.2, color='black', alpha=0.1)
    circle3 = patches.Circle((0.4, 0.35), 0.2, color='black', alpha=0.1)

    # Add circles to the plot
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    # Add text labels for the circles
    ax.text(0.3, 0.5, circle_words[0], fontsize=12, ha='center', va='center')
    ax.text(0.5, 0.5, circle_words[1], fontsize=12, ha='center', va='center')
    ax.text(0.4, 0.35, circle_words[2], fontsize=12, ha='center', va='center')

    # Add the central label
    ax.text(0.4, 0.45, center_word, fontsize=14, ha='center', va='center', fontweight='bold')

    # Set limits and remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')  # Hide the axes

    # Save the image without the background argument
    plt.savefig('venn_diagram.png', bbox_inches='tight', dpi=300)
    plt.show()

# List of inspirational words
inspirational_words = [
    "Absolutely", "Abundant", "Accessible", "Adaptive", "Admire", "Adore", "Affability",
    "Agathist", "Approve", "Best", "Brilliant", "Bold", "Beautiful", "Bright",
    "Charismatic", "Clever", "Creative", "Courageous", "Confident", "Dependable",
    "Dazzling", "Dynamic", "Determined", "Delightful", "Enriching", "Enthusiastic",
    "Excellent", "Extraordinary", "Empowering", "Fantastic", "Fashionable", "Favorite",
    "Fiery", "Friendly", "Gifted", "Grandiose", "Gumptious", "Genuine", "Gracious",
    "Happy", "Hospitable", "Humanitarian", "Hypnotic", "Heroic", "Ideal", "Impressive",
    "Insightful", "Instinctive", "Innovative", "Jolly", "Joysome", "Jubilant", "Just",
    "Kind-hearted", "Knockout", "Kind", "Knowledgeable", "Keen", "Luminous", "Lovely",
    "Loyal", "Liberating", "Magnetic", "Magnificent", "Marvelous", "Miraculous", "Motivated",
    "Moving", "Neighborly", "Noble", "Nurturing", "Nimble", "Nostalgic", "Observant",
    "Open-minded", "Optimistic", "Organized", "Outgoing", "Passionate", "Patient", 
    "Peaceful", "Perceptive", "Persistent", "Personable", "Picturesque", "Playful", 
    "Radiant", "Rapturous", "Razor-sharp", "Reassuring", "Recommendable", "Remarkable",
    "Resilient", "Sagacious", "Savvy", "Self-assured", "Sincere", "Splendid", 
    "Tolerant", "Timeless", "Thoughtful", "Thriving", "Tranquil", "Uplifting", 
    "Unwavering", "Unstoppable", "Unique", "Victorious", "Visionary", "Vibrant", 
    "Virtuous", "Valuable", "Wise", "Witty", "Wonderful", "Welcoming", "Zealous"
]

create_venn_diagram(inspirational_words)
