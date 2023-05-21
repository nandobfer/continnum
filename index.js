const CriterionTypes = {
  BENEFIT: 1,
  COST: 2
}

/** Objeto simbólico para representar chamadas à nossa API em Python */
const API = {
  post: ({ url = '', data = {}, success = () => {} }}) => {
    // ...
  }
}

/** 
 * Classe Model
 * Em React, pode se tornar um Contexto
 */
class Model {
  constructor() {
    this.decision_makers = [];
    this.criteria = [];
    this.alternatives = [];
  }
  
  addDecicionMakers(dms = []) {
    this.decision_makers = dms;
  }
  
  addCriteria(criteria = []) {
    this.criteria = criteria;
  }
  
  addAlternatives(alt = []) {
    this.alternatives = alt;
  }

  addCriterionJudgment({ dm_id, cri_id, sp, sq }) {
    const dm_index = this.decision_makers.findIndex(({ id }) => id === dm_id);
    if (dm_index < 0) {
      throw new Error(`Decision Maker with id ${dm_id} not found in the Model`);
    }

    this.decision_makers[dm_index].criterion_judgments.append({
      cri_id,
      sp,
      sq
    });
  }

  addAlternativeJudgment({ cri_id, dm_id, alt_id, min_value, max_value }) {
    const cri_index = this.criteria.findIndex(({ id }) => id === cri_id);
    if (cri_index < 0) {
      throw new Error(`Criterion with id ${cri_id} not found in the Model`);
    }

    this.criteria[cri_index].alternative_judgments.append({
      dm_id,
      alt_id,
      min_value,
      max_value
    })
  }

  saveToClient() {
    // Salva o objeto no lado do cliente (IndexedDB ou Local Storage)
  }
}

/** Adição dos dados a partir da interação com o usuário  */

// Constrói o objeto com os dados iniciais do modelo
const model = new Model();
model.addDecicionMakers([
  { id: 1, name: "DM_1", weight: 0.4, criterion_judgments: [] },
  { id: 2, name: "DM_2", weight: 0.3, criterion_judgments: [] },
  { id: 3, name: "DM_3", weight: 0.3, criterion_judgments: [] },
]);
model.addCriteria([
  { id: 1, name: "Custo", type: CriterionTypes.COST, alternative_judgments: [] }, 
  { id: 2, name: "Qualidade", type: CriterionTypes.BENEFIT, alternative_judgments: [] }, 
  { id: 3, name: "Ocorrência", type: CriterionTypes.BENEFIT, alternative_judgments: [] }, 
]);
model.addAlternatives([
  { id: 1, name: "ALT_1" },
  { id: 2, name: "ALT_2" },
  { id: 3, name: "ALT_3" },
  { id: 4, name: "ALT_4" },
]);

// Pede os inputs de julgamentos sobre os critérios ao usuário
model.addCriterionJudgment({ dm_id: 1, cri_id: 1, sp: 4, sq: 5 });
model.addCriterionJudgment({ dm_id: 1, cri_id: 2, sp: 5, sq: 5 });
model.addCriterionJudgment({ dm_id: 1, cri_id: 3, sp: 3, sq: 3 });

model.addCriterionJudgment({ dm_id: 2, cri_id: 1, sp: 5, sq: 5 });
model.addCriterionJudgment({ dm_id: 2, cri_id: 2, sp: 3, sq: 3 });
model.addCriterionJudgment({ dm_id: 2, cri_id: 3, sp: 4, sq: 4 });

model.addCriterionJudgment({ dm_id: 3, cri_id: 1, sp: 3, sq: 4 });
model.addCriterionJudgment({ dm_id: 3, cri_id: 2, sp: 3, sq: 4 });
model.addCriterionJudgment({ dm_id: 3, cri_id: 3, sp: 2, sq: 4 });

/** Envio dos dados para cálculo dos pesos dos critérios pelo servidor */

API.post({
  url: '/calculate_total_criteria_normalized_weight',
  data: {
    decision_makers: model.decision_makers,
    criteria: model.criteria,
  },
  success: (response) => {
    // a API irá realizar cálculos e retornar os objetos atualizados
    const { decision_makers, criteria, normalized_cci } = response.data;
    model.decision_makers = decision_makers;
    model.criteria = criteria;
    model.normalized_cci = normalized_cci;
  }
})

// Pede os inputs de julgamentos sobre as alternativas ao usuário
model.addAlternativeJudgment({ cri_id: 1, dm_id: 1, alt_id: 1, min_value: 2, max_value: 2 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 1, alt_id: 2, min_value: 4, max_value: 5 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 1, alt_id: 3, min_value: 3, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 1, alt_id: 4, min_value: 3, max_value: 3 });

model.addAlternativeJudgment({ cri_id: 1, dm_id: 2, alt_id: 1, min_value: 3, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 2, alt_id: 2, min_value: 4, max_value: 5 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 2, alt_id: 3, min_value: 1, max_value: 1 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 2, alt_id: 4, min_value: 5, max_value: 5 });

model.addAlternativeJudgment({ cri_id: 1, dm_id: 3, alt_id: 1, min_value: 2, max_value: 2 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 3, alt_id: 2, min_value: 3, max_value: 4 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 3, alt_id: 3, min_value: 1, max_value: 1 });
model.addAlternativeJudgment({ cri_id: 1, dm_id: 3, alt_id: 4, min_value: 3, max_value: 4 });

model.addAlternativeJudgment({ cri_id: 2, dm_id: 1, alt_id: 1, min_value: 3, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 1, alt_id: 2, min_value: 4, max_value: 4 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 1, alt_id: 3, min_value: 4, max_value: 4 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 1, alt_id: 4, min_value: 5, max_value: 5 });

model.addAlternativeJudgment({ cri_id: 2, dm_id: 2, alt_id: 1, min_value: 1, max_value: 1 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 2, alt_id: 2, min_value: 5, max_value: 5 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 2, alt_id: 3, min_value: 2, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 2, alt_id: 4, min_value: 4, max_value: 4 });

model.addAlternativeJudgment({ cri_id: 2, dm_id: 3, alt_id: 1, min_value: 2, max_value: 2 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 3, alt_id: 2, min_value: 3, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 3, alt_id: 3, min_value: 2, max_value: 2 });
model.addAlternativeJudgment({ cri_id: 2, dm_id: 3, alt_id: 4, min_value: 4, max_value: 5 });

model.addAlternativeJudgment({ cri_id: 3, dm_id: 1, alt_id: 1, min_value: 2, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 1, alt_id: 2, min_value: 2, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 1, alt_id: 3, min_value: 2, max_value: 3 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 1, alt_id: 4, min_value: 2, max_value: 3 });

model.addAlternativeJudgment({ cri_id: 3, dm_id: 2, alt_id: 1, min_value: 2, max_value: 2 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 2, alt_id: 2, min_value: 5, max_value: 5 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 2, alt_id: 3, min_value: 2, max_value: 2 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 2, alt_id: 4, min_value: 1, max_value: 2 });

model.addAlternativeJudgment({ cri_id: 3, dm_id: 3, alt_id: 1, min_value: 1, max_value: 1 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 3, alt_id: 2, min_value: 1, max_value: 1 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 3, alt_id: 3, min_value: 4, max_value: 4 });
model.addAlternativeJudgment({ cri_id: 3, dm_id: 3, alt_id: 4, min_value: 4, max_value: 4 });

API.post({
  url: '/calculate_alternative_ranking',
  data: {
    decision_makers: model.decision_makers,
    criteria: model.criteria,
    alternatives: model.alternatives,
  },
  success: (response) => {
    const \ = response.data;
    model.decision_makers = decision_makers;
    model.criteria = criteria;
    model.alternatives = alternatives;
    model.ranking = ranking;
  }
})