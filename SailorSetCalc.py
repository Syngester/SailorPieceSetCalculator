def EsDeath(IceCore, FrozenBrand, GlacierRemnant, BattleShard, FrostRelic):
    sets = 0
    setsF = 0

    while True:
        if(IceCore >= 3 and FrozenBrand >= 14 and GlacierRemnant >= 9 and BattleShard >= 17 and FrostRelic >= 110):
            IceCore -= 3
            FrozenBrand -= 14
            GlacierRemnant -= 9
            BattleShard -= 17
            FrostRelic -= 110
            setsF += 1
        elif(IceCore >= 1 and FrozenBrand >= 4 and GlacierRemnant >= 9 and BattleShard >= 17 and FrostRelic >= 25):
            IceCore -= 1
            FrozenBrand -= 4
            GlacierRemnant -= 9
            BattleShard -= 17
            FrostRelic -= 25
            sets += 1
        else:
            break
    return sets, setsF

def Kokushibo(MoonCrest, CrescentShard, LunarEssence, DemonRemnant, UpperSeal):
    sets = 0
    setsF = 0

    while True:
        if(MoonCrest >= 3 and CrescentShard >= 14 and LunarEssence >= 9 and DemonRemnant >= 16 and UpperSeal >= 110):
            MoonCrest -= 3
            CrescentShard -= 14
            LunarEssence -= 9
            DemonRemnant -= 16
            UpperSeal -= 110
            setsF += 1
        elif(MoonCrest >= 1 and CrescentShard >= 4 and LunarEssence >= 9 and DemonRemnant >= 16 and UpperSeal >= 25):
            MoonCrest -= 1
            CrescentShard -= 4
            LunarEssence -= 9
            DemonRemnant -= 16
            UpperSeal -= 25
            sets += 1
        else:
            break
    return sets, setsF

def Atomic(AtomicOmen, EminenceEssence, ShadowRemnant, MagicShard, AbyssSigil):
    sets = 0
    while True:
        if(AtomicOmen >= 1 and EminenceEssence >= 3 and ShadowRemnant >= 9 and MagicShard >= 16 and AbyssSigil >= 80):
            AtomicOmen -= 1
            EminenceEssence -= 3
            ShadowRemnant -= 9
            MagicShard -= 16
            AbyssSigil -= 80
            sets += 1
        else:
            break
    return sets

def ShadowMonarch(MonarchCore, MonarchEssence, KamishDagger, ShadowCrystal):
    sets = 0
    while True:
        if(MonarchCore >= 10 and MonarchEssence >= 5 and KamishDagger >= 2 and ShadowCrystal >= 1):
            MonarchCore -= 10
            MonarchEssence -= 5
            KamishDagger -= 2
            ShadowCrystal -= 1
            sets += 1
        else:
            break
    return sets

def Shadow(AtomicCore, ShadowEssence, VoidSeed, UmbralCapsule):
    sets = 0
    while True:
        if(AtomicCore >= 1 and ShadowEssence >= 4 and VoidSeed >= 8 and UmbralCapsule >= 20):
            AtomicCore -= 1
            ShadowEssence -= 4
            VoidSeed -= 8
            UmbralCapsule -= 20
            sets += 1
        else:
            break
    return sets

def Ichigo(SoulFlame, SpiritualCore, SoulFragment):
    sets = 0
    while True:
        if(SoulFlame >= 2 and SpiritualCore >= 4 and SoulFragment >= 8):
            SoulFlame -= 2
            SpiritualCore -= 4
            SoulFragment -= 8
            sets += 1
        else:
            break
    return sets

def Ragna(WyrmBrand, BlackFrost, SilverRequiem):
    sets = 0
    while True:
        if(WyrmBrand >= 7 and BlackFrost >= 3 and SilverRequiem >= 1):
            WyrmBrand -= 7
            BlackFrost -= 3
            SilverRequiem -= 1
            sets += 1
        else:
            break
    return sets

def Yamato(AzureHeart, SilentStorm, YamatoEssence, FrozenWill):
    sets = 0
    while True:
        if(AzureHeart >= 1 and SilentStorm >= 3 and YamatoEssence >= 7 and FrozenWill >= 14):
            AzureHeart -= 1
            SilentStorm -= 3
            YamatoEssence -= 7
            FrozenWill -= 14
            sets += 1
        else:
            break
    return sets

def TrueAizen(EvolutionFragment, TranscendentCore, DivinityEssence, FusionRing, ChrysalisSigil):
    sets = 0
    while True:
        if(EvolutionFragment >= 1 and TranscendentCore >= 3 and DivinityEssence >= 8 and FusionRing >= 15 and ChrysalisSigil >= 75):
            EvolutionFragment -= 1
            TranscendentCore -= 3
            DivinityEssence -= 8
            FusionRing -= 15
            ChrysalisSigil -= 75
            sets += 1
        else:
            break
    return sets

def Aizen(MiragePendants, IllusionPrisms, ReiatsuCore, HogyokuFragment):
    sets = 0
    while True:
        if(MiragePendants >= 10 and IllusionPrisms >= 6 and ReiatsuCore >= 3 and HogyokuFragment >= 1):
            MiragePendants -= 10
            IllusionPrisms -= 6
            ReiatsuCore -= 3
            HogyokuFragment -= 1
            sets += 1
        else:
            break
    return sets

def Rimuru(SagePulse, TempestSeal, SlimeRemnant, SlimeCore):
    sets = 0
    while True:
        if(SagePulse >= 9 and TempestSeal >= 6 and SlimeRemnant >= 3 and SlimeCore >= 1):
            SagePulse -= 9
            TempestSeal -= 6
            SlimeRemnant -= 3
            SlimeCore -= 1
            sets += 1
        else:
            break
    return sets

def StrongestShinobi(PathFragment, EternalCore, BattleSigil, PowerRemnant):
    sets = 0
    setsF = 0
    while True:
        if(PathFragment >= 3 and EternalCore >= 8 and BattleSigil >= 18 and PowerRemnant >= 15):
            PathFragment -= 3
            EternalCore -= 8
            BattleSigil -= 18
            PowerRemnant -= 15
            setsF += 1
        elif(PathFragment >= 1 and EternalCore >= 3 and BattleSigil >= 8 and PowerRemnant >= 15):
            PathFragment -= 1
            EternalCore -= 3
            BattleSigil -= 8
            PowerRemnant -= 15
            sets += 1
        else:
            break
    return sets, setsF

def SaberAlter(DarkGrail, MorganRemnant, AlterEssence, CorruptionCore, CorruptCrown):
    sets = 0
    setsF = 0
    while True:
        if(DarkGrail >= 110 and MorganRemnant >= 15 and AlterEssence >= 8 and CorruptionCore >= 12 and CorruptCrown >= 3):
            DarkGrail -= 110
            MorganRemnant -= 15
            AlterEssence -= 8
            CorruptionCore -= 12
            CorruptCrown -= 3
            setsF += 1
        elif(DarkGrail >= 25 and MorganRemnant >= 15 and AlterEssence >= 8 and CorruptionCore >= 3 and CorruptCrown >= 1):
            DarkGrail -= 25
            MorganRemnant -= 15
            AlterEssence -= 8
            CorruptionCore -= 3
            CorruptCrown -= 1
            sets += 1
        else:
            break
    return sets, setsF

def BlessedMaiden(CelestialMark, AeroCore, GaleEssence, TideRemnant, TempestRelic):
    sets = 0
    setsF = 0
    while True:
        if(CelestialMark >= 3 and AeroCore >= 11 and GaleEssence >= 8 and TideRemnant >= 14 and TempestRelic >= 100):
            CelestialMark -= 3
            AeroCore -= 11
            GaleEssence -= 8
            TideRemnant -= 14
            TempestRelic -= 100
            sets += 1
        elif(CelestialMark >= 1 and AeroCore >= 3 and GaleEssence >= 8 and TideRemnant >= 14 and TempestRelic >= 25):
            CelestialMark -= 1
            AeroCore -= 3
            GaleEssence -= 8
            TideRemnant -= 14
            TempestRelic -= 25
            setsF += 1
        else:
            break
    return sets, setsF

def Anos(CalamitySeal, DemonicFragment, DemonicShard, DestructionEye, ImperialMark):
    sets = 0
    while True:
        if(CalamitySeal >= 65 and DemonicFragment >= 12 and DemonicShard >= 6 and DestructionEye >= 2 and ImperialMark >= 1):
            CalamitySeal -= 65
            DemonicFragment -= 12
            DemonicShard -= 6
            DestructionEye -= 2
            ImperialMark -= 1
            sets += 1
        else:
            break
    return sets

def Gilgamesh(ThroneRemnant, AncientShard, GoldenEssence, PhantasmCore, BrokenSword=0):
    sets = 0
    setsF = 0
    while True:
        if(ThroneRemnant >= 12 and AncientShard >= 6 and GoldenEssence >= 8 and PhantasmCore >= 3 and BrokenSword >= 100):
            ThroneRemnant -= 12
            AncientShard -= 6
            GoldenEssence -= 8
            PhantasmCore -= 3
            BrokenSword -= 100
            setsF += 1
        elif(ThroneRemnant >= 12 and AncientShard >= 6 and GoldenEssence >= 3 and PhantasmCore >= 1):
            ThroneRemnant -= 12
            AncientShard -= 6
            GoldenEssence -= 3
            PhantasmCore -= 1
            sets += 1
        else:
            break
    return sets, setsF

def Madoka(Heart, DivineFragment, SacredBow, RadiantCore, PinkGem):
    sets = 0
    while True:
        if(Heart >= 100 and DivineFragment >= 8 and SacredBow >= 5 and RadiantCore >= 3 and PinkGem >= 1):
            Heart -= 100
            DivineFragment -= 8
            SacredBow -= 5
            RadiantCore -= 3
            PinkGem -= 1
            sets += 1
        else:
            break
    return sets

def StrongestInHistory(ConsumableInput, CursedFlesh, MalevolentSoul, VesselRing, AwakenedCursedFingers, CursedTalisman, InfinityEssence):
    sets = 0
    setsF = 0
    if(ConsumableInput.upper() == "Y"):
        while True:
            if(AwakenedCursedFingers >= 20 and VesselRing >= 7 and MalevolentSoul >= 6 and CursedFlesh >= 1 and CursedTalisman >= 6 and InfinityEssence >= 2):
                AwakenedCursedFingers -= 20
                VesselRing -= 7
                MalevolentSoul -= 6
                CursedFlesh -= 1
                CursedTalisman -= 6
                InfinityEssence -= 2
                setsF += 1
            elif(AwakenedCursedFingers >= 20 and VesselRing >= 7 and MalevolentSoul >= 3 and CursedFlesh >= 1):
                AwakenedCursedFingers -= 20
                VesselRing -= 7
                MalevolentSoul -= 3
                CursedFlesh -= 1
                sets += 1
            else:
                break
    elif(ConsumableInput.upper() == "N"):
        while True:
            if(VesselRing >= 7 and MalevolentSoul >= 6 and CursedFlesh >= 1 and CursedTalisman >= 6 and InfinityEssence >= 2):
                VesselRing -= 7
                MalevolentSoul -= 6
                CursedFlesh -= 1
                CursedTalisman -= 6
                InfinityEssence -= 2
                setsF += 1
            elif(VesselRing >= 7 and MalevolentSoul >= 3 and CursedFlesh >= 1):
                VesselRing -= 7
                MalevolentSoul -= 3
                CursedFlesh -= 1
                sets += 1
            else:
                break
    return sets, setsF

def StrongestOfToday(ConsumableInput, InfinityEssence, BlueSingularity, ReversalPulse, SixEyes, EnergyShards, CursedFlesh):
    sets = 0
    setsF = 0
    if(ConsumableInput.upper() == "Y"):
        while True:
            if(SixEyes >= 6 and ReversalPulse >= 9 and BlueSingularity >= 6 and InfinityEssence >= 1 and EnergyShards >= 6 and CursedFlesh >= 2):
                SixEyes -= 6
                ReversalPulse -= 9
                BlueSingularity -= 6
                InfinityEssence -= 1
                EnergyShards -= 6
                CursedFlesh -= 2
                setsF += 1
            elif(SixEyes >= 6 and ReversalPulse >= 9 and BlueSingularity >= 3 and InfinityEssence >= 1):
                SixEyes -= 6
                ReversalPulse -= 9
                BlueSingularity -= 3
                InfinityEssence -= 1
                sets += 1
            else:
                break
    elif(ConsumableInput.upper() == "N"):
        while True:
            if(ReversalPulse >= 9 and BlueSingularity >= 6 and InfinityEssence >= 1 and EnergyShards >= 6 and CursedFlesh >= 2):
                ReversalPulse -= 9
                BlueSingularity -= 6
                InfinityEssence -= 1
                EnergyShards -= 6
                CursedFlesh -= 2
                setsF += 1
            elif(ReversalPulse >= 9 and BlueSingularity >= 3 and InfinityEssence >= 1):
                ReversalPulse -= 9
                BlueSingularity -= 3
                InfinityEssence -= 1
                sets += 1
            else:
                break
    return sets, setsF

def Alucard(BloodRing, Casull, SoulAmulet):
    sets = 0
    while True:
        if(BloodRing >= 1 and Casull >= 1 and SoulAmulet >= 5):
            BloodRing -= 1
            Casull -= 1
            SoulAmulet -= 5
            sets += 1
        else:
            break
    return sets

def Yuji(DivergentPulse, FlashImpact, EnergyCore):
    sets = 0
    while True:
        if(EnergyCore >= 7 and FlashImpact >= 3 and DivergentPulse >= 1):
            EnergyCore -= 7
            FlashImpact -= 3
            DivergentPulse -= 1
            sets += 1
        else:
            break
    return sets

def QinShi(ImperialSeal, JadeTablet):
    sets = 0
    while True:
        if(ImperialSeal >= 3 and JadeTablet >= 7):
            ImperialSeal -= 3
            JadeTablet -= 7
            sets += 1
        else:
            break
    return sets

def Sukuna(CursedFinger, DismantleFang, CrimsonHeart):
    sets = 0
    while True:
        if(DismantleFang >= 3 and CrimsonHeart >= 1 and CursedFinger >= 6):
            DismantleFang -= 3
            CrimsonHeart -= 1
            CursedFinger -= 6
            sets += 1
        else:
            break
    return sets

def Gojo(VoidFragment, LimitlessRing, InfinityCore):
    sets = 0
    while True:
        if(VoidFragment >= 6 and LimitlessRing >= 3 and InfinityCore >= 1):
            VoidFragment -= 6
            LimitlessRing -= 3
            InfinityCore -= 1
            sets += 1
        else:
            break
    return sets

def main():
    running = True
    while running:
        print("\nSailor Piece Set Calculator")
        print("Select a set:")
        print("0. Exit")
        print("1. Esdeath")
        print("2. Kokushibo")
        print("3. Atomic")
        print("4. ShadowMonarch")
        print("5. Shadow")
        print("6. Ichigo")
        print("7. Ragna")
        print("8. Yamato")
        print("9. TrueAizen")
        print("10. Aizen")
        print("11. Rimuru")
        print("12. StrongestShinobi")
        print("13. SaberAlter")
        print("14. BlessedMaiden")
        print("15. Anos")
        print("16. Gilgamesh")
        print("17. Madoka")
        print("18. StrongestInHistory")
        print("19. StrongestOfToday")
        print("20. Alucard")
        print("21. Yuji")
        print("22. QinShi")
        print("23. Sukuna")
        print("24. Gojo")
        try:
            inp = int(input("Choice: "))
            if inp < 0 or inp > 24:
                print("Invalid choice. Select 0-24.")
                continue
        except ValueError:
            print("Invalid input, numbers only.")
            continue

        match inp:
            case 0:
                print("Exiting")
                running = False
            case 1:
                print("Esdeath set")
                IceCore = int(input("Ice Core: "))
                FrozenBrand = int(input("Frozen Brand: "))
                GlacierRemnant = int(input("Glacier Remnant: "))
                BattleShard = int(input("Battle Shard: "))
                FrostRelic = int(input("Frost Relic: "))
                sets, setsF = EsDeath(IceCore, FrozenBrand, GlacierRemnant, BattleShard, FrostRelic)
                print(f"{sets} Esdeath sets and {setsF} with F moves")
            case 2:
                print("Kokushibo set")
                MoonCrest = int(input("Moon Crest: "))
                CrescentShard = int(input("Crescent Shard: "))
                LunarEssence = int(input("Lunar Essence: "))
                DemonRemnant = int(input("Demon Remnant: "))
                UpperSeal = int(input("Upper Seal: "))
                sets, setsF = Kokushibo(MoonCrest, CrescentShard, LunarEssence, DemonRemnant, UpperSeal)
                print(f"{sets} Kokushibo sets and {setsF} with F moves")
            case 3:
                print("Atomic set")
                AtomicOmen = int(input("Atomic Omen: "))
                EminenceEssence = int(input("Eminence Essence: "))
                ShadowRemnant = int(input("Shadow Remnant: "))
                MagicShard = int(input("Magic Shard: "))
                AbyssSigil = int(input("Abyss Sigil: "))
                sets = Atomic(AtomicOmen, EminenceEssence, ShadowRemnant, MagicShard, AbyssSigil)
                print(f"{sets} Atomic sets")
            case 4:
                print("ShadowMonarch set")
                MonarchCore = int(input("Monarch Core: "))
                MonarchEssence = int(input("Monarch Essence: "))
                KamishDagger = int(input("Kamish Dagger: "))
                ShadowCrystal = int(input("Shadow Crystal: "))
                sets = ShadowMonarch(MonarchCore, MonarchEssence, KamishDagger, ShadowCrystal)
                print(f"{sets} ShadowMonarch sets")
            case 5:
                print("Shadow set")
                AtomicCore = int(input("Atomic Core: "))
                ShadowEssence = int(input("Shadow Essence: "))
                VoidSeed = int(input("Void Seed: "))
                UmbralCapsule = int(input("Umbral Capsule: "))
                sets = Shadow(AtomicCore, ShadowEssence, VoidSeed, UmbralCapsule)
                print(f"{sets} Shadow sets")
            case 6:
                print("Ichigo set")
                SoulFlame = int(input("Soul Flame: "))
                SpiritualCore = int(input("Spiritual Core: "))
                SoulFragment = int(input("Soul Fragment: "))
                sets = Ichigo(SoulFlame, SpiritualCore, SoulFragment)
                print(f"{sets} Ichigo sets")
            case 7:
                print("Ragna set")
                WyrmBrand = int(input("Wyrm Brand: "))
                BlackFrost = int(input("Black Frost: "))
                SilverRequiem = int(input("Silver Requiem: "))
                sets = Ragna(WyrmBrand, BlackFrost, SilverRequiem)
                print(f"{sets} Ragna sets")
            case 8:
                print("Yamato set")
                AzureHeart = int(input("Azure Heart: "))
                SilentStorm = int(input("Silent Storm: "))
                YamatoEssence = int(input("Yamato Essence: "))
                FrozenWill = int(input("Frozen Will: "))
                sets = Yamato(AzureHeart, SilentStorm, YamatoEssence, FrozenWill)
                print(f"{sets} Yamato sets")
            case 9:
                print("TrueAizen set")
                EvolutionFragment = int(input("Evolution Fragment: "))
                TranscendentCore = int(input("Transcendent Core: "))
                DivinityEssence = int(input("Divinity Essence: "))
                FusionRing = int(input("Fusion Ring: "))
                ChrysalisSigil = int(input("Chrysalis Sigil: "))
                sets = TrueAizen(EvolutionFragment, TranscendentCore, DivinityEssence, FusionRing, ChrysalisSigil)
                print(f"{sets} TrueAizen sets")
            case 10:
                print("Aizen set")
                MiragePendants = int(input("Mirage Pendants: "))
                IllusionPrisms = int(input("Illusion Prisms: "))
                ReiatsuCore = int(input("Reiatsu Core: "))
                HogyokuFragment = int(input("Hogyoku Fragment: "))
                sets = Aizen(MiragePendants, IllusionPrisms, ReiatsuCore, HogyokuFragment)
                print(f"{sets} Aizen sets")
            case 11:
                print("Rimuru set")
                SagePulse = int(input("Sage Pulse: "))
                TempestSeal = int(input("Tempest Seal: "))
                SlimeRemnant = int(input("Slime Remnant: "))
                SlimeCore = int(input("Slime Core: "))
                sets = Rimuru(SagePulse, TempestSeal, SlimeRemnant, SlimeCore)
                print(f"{sets} Rimuru sets")
            case 12:
                print("StrongestShinobi set")
                PathFragment = int(input("Path Fragment: "))
                EternalCore = int(input("Eternal Core: "))
                BattleSigil = int(input("Battle Sigil: "))
                PowerRemnant = int(input("Power Remnant: "))
                sets, setsF = StrongestShinobi(PathFragment, EternalCore, BattleSigil, PowerRemnant)
                print(f"{sets} StrongestShinobi sets and {setsF} with F moves")
            case 13:
                print("SaberAlter set")
                DarkGrail = int(input("Dark Grail: "))
                MorganRemnant = int(input("Morgan Remnant: "))
                AlterEssence = int(input("Alter Essence: "))
                CorruptionCore = int(input("Corruption Core: "))
                CorruptCrown = int(input("Corrupt Crown: "))
                sets, setsF = SaberAlter(DarkGrail, MorganRemnant, AlterEssence, CorruptionCore, CorruptCrown)
                print(f"{sets} SaberAlter sets and {setsF} with F moves")
            case 14:
                print("BlessedMaiden set")
                CelestialMark = int(input("Celestial Mark: "))
                AeroCore = int(input("Aero Core: "))
                GaleEssence = int(input("Gale Essence: "))
                TideRemnant = int(input("Tide Remnant: "))
                TempestRelic = int(input("Tempest Relic: "))
                sets, setsF = BlessedMaiden(CelestialMark, AeroCore, GaleEssence, TideRemnant, TempestRelic)
                print(f"{sets} BlessedMaiden sets and {setsF} with F moves")
            case 15:
                print("Anos set")
                CalamitySeal = int(input("Calamity Seal: "))
                DemonicFragment = int(input("Demonic Fragment: "))
                DemonicShard = int(input("Demonic Shard: "))
                DestructionEye = int(input("Destruction Eye: "))
                ImperialMark = int(input("Imperial Mark: "))
                sets = Anos(CalamitySeal, DemonicFragment, DemonicShard, DestructionEye, ImperialMark)
                print(f"{sets} Anos sets")
            case 16:
                print("Gilgamesh set")
                ThroneRemnant = int(input("Throne Remnant: "))
                AncientShard = int(input("Ancient Shard: "))
                GoldenEssence = int(input("Golden Essence: "))
                PhantasmCore = int(input("Phantasm Core: "))
                BrokenSword = int(input("Broken Sword: "))
                sets, setsF = Gilgamesh(ThroneRemnant, AncientShard, GoldenEssence, PhantasmCore, BrokenSword)
                print(f"{sets} Gilgamesh sets and {setsF} with F moves")
            case 17:
                print("Madoka set")
                Heart = int(input("Heart: "))
                DivineFragment = int(input("Divine Fragment: "))
                SacredBow = int(input("Sacred Bow: "))
                RadiantCore = int(input("Radiant Core: "))
                PinkGem = int(input("Pink Gem: "))
                sets = Madoka(Heart, DivineFragment, SacredBow, RadiantCore, PinkGem)
                print(f"{sets} Madoka sets")
            case 18:
                print("StrongestInHistory set")
                ConsumableInput = input("Consumables? (Y/N): ").strip()
                CursedFlesh = int(input("Cursed Flesh: "))
                MalevolentSoul = int(input("Malevolent Soul: "))
                VesselRing = int(input("Vessel Ring: "))
                AwakenedCursedFingers = int(input("Awakened Cursed Fingers: "))
                CursedTalisman = int(input("Cursed Talisman: "))
                InfinityEssence = int(input("Infinity Essence: "))
                sets, setsF = StrongestInHistory(ConsumableInput, CursedFlesh, MalevolentSoul, VesselRing, AwakenedCursedFingers, CursedTalisman, InfinityEssence)
                print(f"{sets} StrongestInHistory sets and {setsF} with F moves")
            case 19:
                print("StrongestOfToday set")
                ConsumableInput = input("Consumables? (Y/N): ").strip()
                InfinityEssence = int(input("Infinity Essence: "))
                BlueSingularity = int(input("Blue Singularity: "))
                ReversalPulse = int(input("Reversal Pulse: "))
                SixEyes = int(input("Six Eyes: "))
                EnergyShards = int(input("Energy Shards: "))
                CursedFlesh = int(input("Cursed Flesh: "))
                sets, setsF = StrongestOfToday(ConsumableInput, InfinityEssence, BlueSingularity, ReversalPulse, SixEyes, EnergyShards, CursedFlesh)
                print(f"{sets} StrongestOfToday sets and {setsF} with F moves")
            case 20:
                print("Alucard set")
                BloodRing = int(input("Blood Ring: "))
                Casull = int(input("Casull: "))
                SoulAmulet = int(input("Soul Amulet: "))
                sets = Alucard(BloodRing, Casull, SoulAmulet)
                print(f"{sets} Alucard sets")
            case 21:
                print("Yuji set")
                DivergentPulse = int(input("Divergent Pulse: "))
                FlashImpact = int(input("Flash Impact: "))
                EnergyCore = int(input("Energy Core: "))
                sets = Yuji(DivergentPulse, FlashImpact, EnergyCore)
                print(f"{sets} Yuji sets")
            case 22:
                print("QinShi set")
                ImperialSeal = int(input("Imperial Seal: "))
                JadeTablet = int(input("Jade Tablet: "))
                sets = QinShi(ImperialSeal, JadeTablet)
                print(f"{sets} QinShi sets")
            case 23:
                print("Sukuna set")
                CursedFinger = int(input("Cursed Finger: "))
                DismantleFang = int(input("Dismantle Fang: "))
                CrimsonHeart = int(input("Crimson Heart: "))
                sets = Sukuna(CursedFinger, DismantleFang, CrimsonHeart)
                print(f"{sets} Sukuna sets")
            case 24:
                print("Gojo set")
                VoidFragment = int(input("Void Fragment: "))
                LimitlessRing = int(input("Limitless Ring: "))
                InfinityCore = int(input("Infinity Core: "))
                sets = Gojo(VoidFragment, LimitlessRing, InfinityCore)
                print(f"{sets} Gojo sets")

if __name__ == "__main__":
    main()
