from typing import List, Tuple

# Define the Amharic alphabet as a grid
amharic_alphabet = [
    ["ሀ", "ሁ", "ሂ", "ሃ", "ሄ", "ህ", "ሆ"],
    ["ለ", "ሉ", "ሊ", "ላ", "ሌ", "ል", "ሎ"],
    ["ሐ", "ሑ", "ሒ", "ሓ", "ሔ", "ሕ", "ሖ"],
    ["መ", "ሙ", "ሚ", "ማ", "ሜ", "ም", "ሞ"],
    ["ሠ", "ሡ", "ሢ", "ሣ", "ሤ", "ሥ", "ሦ"],
    ["ረ", "ሩ", "ሪ", "ራ", "ሬ", "ር", "ሮ"],
    ["ሰ", "ሱ", "ሲ", "ሳ", "ሴ", "ስ", "ሶ"],
    ["ሸ", "ሹ", "ሺ", "ሻ", "ሼ", "ሽ", "ሾ"],
    ["ቀ", "ቁ", "ቂ", "ቃ", "ቄ", "ቅ", "ቆ"],
    ["ቐ", "ቑ", "ቒ", "ቓ", "ቔ", "ቕ", "ቖ"],
    ["በ", "ቡ", "ቢ", "ባ", "ቤ", "ብ", "ቦ"],
    ["ቨ", "ቩ", "ቪ", "ቫ", "ቬ", "ቭ", "ቮ"],
    ["ተ", "ቱ", "ቲ", "ታ", "ቴ", "ት", "ቶ"],
    ["ቸ", "ቹ", "ቺ", "ቻ", "ቼ", "ች", "ቾ"],
    ["ኀ", "ኁ", "ኂ", "ኃ", "ኄ", "ኅ", "ኆ"],
    ["ነ", "ኑ", "ኒ", "ና", "ኔ", "ን", "ኖ"],
    ["ኘ", "ኙ", "ኚ", "ኛ", "ኜ", "ኝ", "ኞ"],
    ["አ", "ኡ", "ኢ", "ኣ", "ኤ", "እ", "ኦ"],
    ["ከ", "ኩ", "ኪ", "ካ", "ኬ", "ክ", "ኮ"],
    ["ኸ", "ኹ", "ዪ", "ኻ", "ዼ", "ኽ", "ኾ"],
    ["ወ", "ዉ", "ዊ", "ዋ", "ዌ", "ው", "ዎ"],
    ["ዐ", "ዑ", "ዒ", "ዓ", "ዔ", "ዕ", "ዖ"],
    ["ዘ", "ዙ", "ዚ", "ዛ", "ዜ", "ዝ", "ዞ"],
    ["የ", "ዩ", "ዧ", "ያ", "ዬ", "ይ", "ዮ"],
    ["ደ", "ዱ", "ዲ", "ዳ", "ዴ", "ድ", "ዶ"],
    ["ዸ", "ዹ", "ዺ", "ዻ", "ዼ", "ዽ", "ዾ"],
    ["ጀ", "ጁ", "ጂ", "ጃ", "ጄ", "ጅ", "ጆ"],
    ["ገ", "ጉ", "ጊ", "ጋ", "ጌ", "ግ", "ጎ"],
    ["ጘ", "ጙ", "ጚ", "ጛ", "ጜ", "ጝ", "ጞ"],
    ["ጠ", "ጡ", "ጢ", "ጣ", "ጤ", "ጥ", "ጦ"],
    ["ጨ", "ጩ", "ጪ", "ጫ", "ጬ", "ጭ", "ጮ"],
    ["ጰ", "ጱ", "ጲ", "ጳ", "ጴ", "ጵ", "ጶ"],
    ["ጸ", "ጹ", "ጺ", "ጻ", "ጼ", "ጽ", "ጾ"],
    ["ፀ", "ፁ", "ፂ", "ፃ", "ፄ", "ፅ", "ፆ"],
    ["ፈ", "ፉ", "ፊ", "ፋ", "ፌ", "ፍ", "ፎ"],
    ["ፐ", "ፑ", "ፒ", "ፓ", "ፔ", "ፕ", "ፖ"],
]

# Build a lookup table for fast grid position access
amharic_positions = {
    char: (row, col)
    for row, line in enumerate(amharic_alphabet)
    for col, char in enumerate(line)
}

print(amharic_positions)

def manhattan_distance(char1: str, char2: str) -> int:
    pos1 = amharic_positions[char1]
    pos2 = amharic_positions[char2]
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def average_word_manhattan_distance(word: str) -> float:
    total_distance = sum(
        manhattan_distance(word[i - 1], word[i]) for i in range(1, len(word))
    )
    result=total_distance / (len(word) - 1)
    print(f'avg_distance of {word} is {result}')
    return total_distance / (len(word) - 1)

def order_words_by_distance(words: List[str]) -> List[str]:
    return sorted(words, key=average_word_manhattan_distance)


words = ["ሰማ", "አበበ", "ሰማይ", "ይልቃል","ፋሲል"]
sorted_words = order_words_by_distance(words)
print(sorted_words)  

print(len(amharic_alphabet))