class Generation:
    def pokemon_range(self, gen: int) -> range:
        """Return range of pokemons id
        Args:
            gen: int
        Returns:
            poke_range: range  
        """
        self.gen = gen
        match gen:
            case 1:
                return range(0, 100)
            case 2:
                return range(101, 200)
            case 3:
                return range(201, 300)
            case 4:
                return range(301, 400)
            case 5:
                return range(401, 500)
            case 6:
                return range(501, 600)
            case 7:
                return range(601, 700)
            case 8:
                return range(701, 800)
            case 9:
                return range(801, 900)