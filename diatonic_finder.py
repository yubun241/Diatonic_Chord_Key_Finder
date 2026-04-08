class DiatonicKeyFinder:
    """
    A utility class to identify musical keys based on a list of diatonic chords.
    All notations are unified to sharps (#) as requested.
    """

    def __init__(self):
        # Dictionary defining diatonic chords for each key (Triads)
        # Sharp (#) notation is used exclusively.
        self.diatonic_data = {
            # Major Keys
            "C Major":  {"C", "Dm", "Em", "F", "G", "Am", "Bm(b5)"},
            "G Major":  {"G", "Am", "Bm", "C", "D", "Em", "F#m(b5)"},
            "D Major":  {"D", "Em", "F#m", "G", "A", "Bm", "C#m(b5)"},
            "A Major":  {"A", "Bm", "C#m", "D", "E", "F#m", "G#m(b5)"},
            "E Major":  {"E", "F#m", "G#m", "A", "B", "C#m", "D#m(b5)"},
            "B Major":  {"B", "C#m", "D#m", "E", "F#", "G#m", "A#m(b5)"},
            "F# Major": {"F#", "G#m", "A#m", "B", "C#", "D#m", "Fm(b5)"},
            "C# Major": {"C#", "D#m", "Fm", "F#", "G#", "A#m", "Cm(b5)"},
            "G# Major": {"G#", "A#m", "Cm", "C#", "D#", "Fm", "Gm(b5)"},
            "D# Major": {"D#", "Fm", "Gm", "G#", "A#", "Cm", "Dm(b5)"},
            "A# Major": {"A#", "Cm", "Dm", "D#", "F", "Gm", "Am(b5)"},
            "F Major":  {"F", "Gm", "Am", "A#", "C", "Dm", "Em(b5)"},
            
            # Minor Keys (Natural Minor)
            "A Minor":  {"Am", "Bm(b5)", "C", "Dm", "Em", "F", "G"},
            "E Minor":  {"Em", "F#m(b5)", "G", "Am", "Bm", "C", "D"},
            "B Minor":  {"Bm", "C#m(b5)", "D", "Em", "F#m", "G", "A"},
            "F# Minor": {"F#m", "G#m(b5)", "A", "Bm", "C#m", "D", "E"},
            "C# Minor": {"C#m", "D#m(b5)", "E", "F#m", "G#m", "A", "B"},
            "G# Minor": {"G#m", "A#m(b5)", "B", "C#m", "D#m", "E", "F#"},
            "D# Minor": {"D#m", "Fm(b5)", "F#", "G#m", "A#m", "B", "C#"},
            "A# Minor": {"A#m", "Cm(b5)", "C#", "D#m", "Fm", "F#", "G#"},
            "F Minor":  {"Fm", "Gm(b5)", "G#", "A#m", "Cm", "C#", "D#"},
            "C Minor":  {"Cm", "Dm(b5)", "D#", "Fm", "Gm", "G#", "A#"},
            "G Minor":  {"Gm", "Am(b5)", "A#", "Cm", "Dm", "D#", "F"},
            "D Minor":  {"Dm", "Em(b5)", "F", "Gm", "Am", "A#", "C"},
        }

    def find_keys(self, chords):
        """
        Returns a list of keys that contain all the provided chords.
        """
        if not chords:
            return []
            
        input_set = set(chords)
        matched_keys = []

        for key_name, diatonic_chords in self.diatonic_data.items():
            if input_set.issubset(diatonic_chords):
                matched_keys.append(key_name)
        
        return matched_keys

def main():
    finder = DiatonicKeyFinder()
    
    print("--- Diatonic Key Finder ---")
    print("コードをスペース区切りで入力してください（例: C Dm G）")
    print("※終了するには 'exit' と入力してください。")
    
    while True:
        user_input = input("\n入力 > ").strip()
        
        if user_input.lower() == 'exit':
            print("プログラムを終了します。")
            break
        
        if not user_input:
            continue

        # スペースまたはカンマで区切ってリスト化
        input_chords = user_input.replace(',', ' ').split()
        
        results = finder.find_keys(input_chords)
        
        if results:
            print(f"可能性のあるキー: {', '.join(results)}")
        else:
            print("一致するダイアトニックキーが見つかりませんでした。")
            print("※表記が正しいか確認してください（例: F#m, Bm(b5), A#）")

if __name__ == "__main__":
    main()
