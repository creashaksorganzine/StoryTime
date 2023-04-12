# arc dictionaries
import hold.arcsDicts as arcsDicts
# hero_journey = {
#     "arc": "The Hero\'s Journey",
#     "Call to Adventure": "The hero receives a call to leave their ordinary world and embark on a journey or quest.",
#     "Refusal of the Call": "The hero may initially refuse the call to adventure, often due to fear or a sense of inadequacy.",
#     "Meeting the Mentor": "The hero meets a wise mentor who provides guidance and assistance on their journey.",
#     "Crossing the Threshold": "The hero leaves their ordinary world and enters the unknown, beginning their adventure.",
#     "Tests, Allies, and Enemies": "The hero encounters a series of tests, which often involve making alliances with helpful characters and facing off against enemies.",
#     "Approach to the Inmost Cave": "The hero approaches a critical point in their journey, often a physical location or a confrontation with their greatest fear.",
#     "Ordeal": "The hero faces their greatest challenge, often a life or death struggle, and emerges victorious or transformed.",
#     "Reward": "The hero receives a reward, often a valuable object or knowledge gained from their journey.",
#     "The Road Back": "The hero begins their journey back to their ordinary world, often encountering further challenges along the way.",
#     "Resurrection": "The hero faces a final and often the most dangerous challenge, where they must use everything they have learned to succeed.",
#     "Return with the Elixir": "The hero returns to their ordinary world, often with a newfound wisdom or treasure, which they can use to benefit themselves and others."
# };
# overcoming_monster = {
#     "arc": "Overcoming the Monster",
#     "The Monster": "The hero learns about a menacing monster or villain that threatens the community.",
#     "Call to Action": "The hero is called upon to defeat the monster and save the community.",
#     "Gathering Allies": "The hero gathers allies and resources to aid them in their quest to defeat the monster.",
#     "Journey to the Lair": "The hero sets out on a journey to the monster's lair, facing obstacles and challenges along the way.",
#     "Final Confrontation": "The hero confronts the monster in a final battle, using their skills and resources to overcome it.",
#     "Victory and Spoils": "The hero emerges victorious and is rewarded for their efforts, often with treasure, recognition, or a new status in the community."
# };
# rags_to_riches = {
#     "arc": "Rags to Riches",
#     "Initial Situation": "The hero starts in a state of poverty or disadvantage.",
#     "Opportunity": "The hero encounters an opportunity to improve their situation, often through a stroke of luck or the help of a mentor.",
#     "Rising Fortunes": "The hero experiences a period of success and rising fortunes, often through hard work, talent, or good fortune.",
#     "Reversal of Fortune": "The hero experiences a setback or crisis that threatens their newfound success.",
#     "Dark Night of the Soul": "The hero experiences a moment of despair or doubt, questioning whether they will ever be able to achieve their goals.",
#     "Overcoming the Obstacle": "The hero overcomes the obstacle or crisis through perseverance, ingenuity, or help from others.",
#     "Final Triumph": "The hero achieves their ultimate goal and enjoys lasting success and happiness.",
# };
# the_quest = {
#     "arc": "The Quest",
#     "Call to Adventure": "The hero receives a call to embark on a quest or journey.",
#     "Setting Out": "The hero sets out on their journey, often leaving their home or comfort zone behind.",
#     "Trials and Tribulations": "The hero encounters a series of trials and challenges, which test their skills and character.",
#     "Gathering Allies": "The hero gathers allies and companions to help them on their quest.",
#     "Approach to the Inmost Cave": "The hero approaches the central challenge or conflict of the quest.",
#     "Supreme Ordeal": "The hero faces their greatest challenge, often a life or death struggle, and emerges victorious or transformed.",
#     "Reward": "The hero receives a reward or gains knowledge as a result of their journey and ordeal.",
#     "The Road Back": "The hero begins their journey back to their home or community.",
#     "Resurrection": "The hero faces a final challenge or confrontation that tests everything they have learned.",
#     "Return with the Elixir": "The hero returns to their home or community, often bringing back a valuable treasure or gift that benefits others."
# };
# rebirth = {
#     "arc": "Rebirth",
#     "The Fall": "The hero experiences a fall from grace, often due to a mistake or personal failing.",
#     "Awareness of the Problem": "The hero becomes aware of the problem or flaw that led to their fall.",
#     "Journey or Quest": "The hero embarks on a journey or quest to overcome their flaw and achieve redemption.",
#     "Facing Challenges": "The hero faces a series of challenges and obstacles, often reflecting their internal struggle.",
#     "Transformation": "The hero undergoes a transformation, often involving a symbolic death and rebirth.",
#     "Atonement": "The hero makes amends or seeks forgiveness for their past mistakes.",
#     "Return": "The hero returns to their community or society, often bringing back a gift or message of hope.",
#     "Redemption": "The hero achieves redemption and regains their place in society, often as a wiser and more compassionate person."
# };
# tragedy = {
#     "arc": "Tragedy",
#     "The Tragic Hero": "The protagonist is a noble or admirable character with a fatal flaw or weakness.",
#     "Flaw": "The hero's flaw leads to their downfall and destruction.",
#     "The Reversal": "The hero experiences a reversal of fortune, often due to a mistake or poor decision.",
#     "Internal Conflict": "The hero experiences internal conflict as they struggle to avoid their tragic fate.",
#     "External Conflict": "The hero may face external conflict or obstacles that contribute to their downfall.",
#     "Catharsis": "The audience experiences a release of emotions or a sense of purging through the tragic events.",
#     "The Hero's Downfall": "The hero meets a tragic end, often resulting in their death or destruction.",
#     "Recognition": "The hero experiences a moment of recognition or realization, often too late to save them.",
#     "Irony": "The story often contains irony, where the opposite of what is expected or intended occurs.",
#     "Lesson": "The story may contain a lesson or moral, often related to the consequences of hubris or the dangers of human weakness."
# };
# comedy = {
#     "arc": "Comedy",
#     "Introduction": "The story introduces the characters and sets up the initial situation.",
#     "Problem or Conflict": "The story presents a problem or conflict that must be resolved.",
#     "Complications": "The story introduces complications or obstacles that make the problem more difficult to solve.",
#     "Errors and Mistakes": "The characters make errors and mistakes that contribute to the comedy.",
#     "Farcical Elements": "The story may contain farcical elements, such as exaggerated physical humor or absurd situations.",
#     "Unexpected Twists": "The story contains unexpected twists or turns that add to the humor.",
#     "Climax": "The story reaches a climactic moment where the problem is finally resolved.",
#     "Resolution": "The story concludes with a satisfying resolution that ties up loose ends and provides closure.",
#     "Lesson": "The story may contain a lesson or moral, often related to the power of humor or the importance of not taking oneself too seriously."
# };
# voyage_and_return = {
#     "arc": "Voyage and Return",
#     "The Call to Adventure": "The hero receives a call to embark on a journey or voyage to a strange land or world.",
#     "Departure": "The hero departs from their home or ordinary world and sets out on the journey.",
#     "Strange Land": "The hero arrives in a strange and unfamiliar land or world.",
#     "Trials and Obstacles": "The hero faces a series of trials and obstacles in the strange land.",
#     "The Journey Back": "The hero begins their journey back to their home or ordinary world.",
#     "Return": "The hero returns to their home or ordinary world, often bringing back new knowledge or treasures.",
#     "New Perspective": "The hero gains a new perspective or understanding as a result of their journey and experiences.",
#     "Reintegration": "The hero must reintegrate into their old life and find a way to use their new knowledge and perspective in a positive way."
# };
# underdog_story = {
#     "arc": "Underdog Story",
#     "The Underdog": "The hero is an unlikely or disadvantaged character who faces a powerful or privileged opponent.",
#     "Introduction": "The story introduces the characters and sets up the initial situation.",
#     "Struggle and Obstacles": "The hero faces a series of struggles and obstacles in their quest to overcome their opponent.",
#     "Training and Preparation": "The hero undergoes training or preparation to improve their skills and abilities.",
#     "Rising Action": "The story builds to a climax as the hero faces their opponent in a final confrontation.",
#     "The Final Showdown": "The hero confronts their opponent in a final battle or competition.",
#     "Victory": "The hero emerges victorious, often through their own effort and skill.",
#     "Recognition": "The hero receives recognition or respect from others as a result of their victory.",
#     "Lessons Learned": "The story may contain a lesson or moral, often related to the importance of perseverance, hard work, or overcoming adversity."
# };
# redemption_arc = {
    "arc": "Redemption",
    "The Fall": "The hero experiences a fall from grace, often due to a mistake or personal failing.",
    "Awareness of the Problem": "The hero becomes aware of the problem or flaw that led to their fall.",
    "Journey or Quest": "The hero embarks on a journey or quest to overcome their flaw and achieve redemption.",
    "Facing Challenges": "The hero faces a series of challenges and obstacles, often reflecting their internal struggle.",
    "Transformation": "The hero undergoes a transformation, often involving a symbolic death and rebirth.",
    "Atonement": "The hero makes amends or seeks forgiveness for their past mistakes.",
    "Redemption": "The hero achieves redemption and regains their place in society, often as a wiser and more compassionate person.",
    "New Purpose": "The hero finds a new purpose or mission in life, often related to making amends for their past mistakes.",
    "Lessons Learned": "The story may contain a lesson or moral, often related to the power of forgiveness, second chances, or personal growth."
}

arcsDicts = arcsDicts.arcsDicts;

# arcs list
# arcsDicts = [hero_journey, overcoming_monster, rags_to_riches, the_quest, rebirth, tragedy, comedy, voyage_and_return, underdog_story, redemption_arc];

# print(hero_journey["arc"]);
# print(arcs[0]["arc"]);

print(arcsDicts)
