def create_pokemons_and_attacks_dicts(all_documents_list, empty_pokemons_list, empty_attacks_list):

    pokemons_list = empty_pokemons_list
    attacks_list = empty_attacks_list

    for document in all_documents_list:
        print(f"Extracting pokemon: {document['id']}, {document['name']}")

        pokemon = {
            'pokemon_id': document['id'],
            'pokemon_name': document['name'],
            'type1': None,
            'type2': None,
            'weight': document['weight']
        }

        for stat in document['stats']:
            pokemon[stat['stat']['name']] = stat['base_stat']

        for type in document['types']:
            type_slot = type['slot']
            key = 'type' + str(type_slot)
            pokemon[key] = type['type']['name']

        pokemons_list.append(pokemon)

        for move in document['moves']:

            for version_group_detail in move['version_group_details']:

                attack = {
                    'pokemon_id': document['id'],
                    'move_name': move['move']['name'],
                    'level_learned_at': None,
                    'move_learn_method': None,
                    'version_group': None
                }

                attack['level_learned_at'] = version_group_detail['level_learned_at']
                attack['move_learn_method'] = version_group_detail['move_learn_method']['name']
                attack['version_group'] = version_group_detail['version_group']['name']

                attacks_list.append(attack)

    return pokemons_list, attacks_list