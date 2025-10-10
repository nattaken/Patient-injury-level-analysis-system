print("=== ระบบประเมินระดับความเสี่ยงผู้ป่วย (Triage) ===")
print("ตอบ y = ใช่ / n = ไม่ใช่")

# ข้อมูลเบื้องต้น
sbp = int(input("ค่าความดันตัวบน (SBP mmHg): "))
hr = int(input("อัตราการเต้นของหัวใจ (ชีพจร bpm): "))

# อาการร่วม
unconscious = input("ผู้ป่วยหมดสติหรือไม่? (y/n): ")
severe_breathing_difficulty = input("หายใจลำบากอย่างรุนแรงหรือไม่? (y/n): ")
severe_pain = input("ปวดระดับรุนแรง 9-10 หรือไม่? (y/n): ")
moderate_symptoms = input("มีอาการเวียนหัว อาเจียน หรือปวดระดับ 6-8 หรือไม่? (y/n): ")
mild_symptoms = input("มีอาการเล็กน้อยหรือมาตามนัดหรือไม่? (y/n): ")
certificate_or_medication = input("มาขอใบรับรองแพทย์หรือซื้อยาเท่านั้น? (y/n): ")

# ประเมินระดับความเสี่ยง
if sbp < 90 and (hr > 150 or hr < 50):
    level = 1
    description = "ระดับ 1: วิกฤต - ความดันต่ำและชีพจรผิดปกติรุนแรง"
    action = "รับพบแพทย์ทันที"
elif unconscious == "y" or severe_breathing_difficulty == "y":
    level = 1
    description = "ระดับ 1: วิกฤต - หายใจลำบากหรือหมดสติ"
    action = "รับพบแพทย์ทันที"
elif hr > 150 or hr < 50:
    level = 2
    description = "ระดับ 2: ฉุกเฉิน - ชีพจรผิดปกติ"
    action = "พบแพทย์ภายใน 10 นาที"
elif severe_pain == "y":
    level = 2
    description = "ระดับ 2: ฉุกเฉิน - ปวดรุนแรง"
    action = "พบแพทย์ภายใน 10 นาที"
elif sbp < 90 or (120 <= hr <= 150):
    level = 3
    description = "ระดับ 3: เร่งด่วน - อาการทางไหลเวียนโลหิต"
    action = "พบแพทย์ภายใน 30 นาที"
elif moderate_symptoms == "y":
    level = 3
    description = "ระดับ 3: เร่งด่วน - เจ็บป่วยปานกลาง"
    action = "พบแพทย์ภายใน 30 นาที"
elif mild_symptoms == "y":
    level = 4
    description = "ระดับ 4: ไม่เร่งด่วน"
    action = "พบแพทย์ภายใน 60 นาที"
elif certificate_or_medication == "y":
    level = 5
    description = "ระดับ 5: ไม่ใช่เหตุทางการแพทย์"
    action = "รอพบแพทย์ตามคิวได้"
else:
    level = 3
    description = "ระดับ 3: ยังไม่สามารถประเมินได้ชัดเจน"
    action = "พบแพทย์ภายใน 30 นาที"

# แสดงผล
print("\n=== ผลการประเมิน ===")
print(description)
print(action)
